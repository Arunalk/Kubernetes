# **<span style="color:#A7C7E7;">Why Convert HTTPS to HTTP (SSL Termination)?**</span>

>       Converting HTTPS to HTTP at the Load Balancer (SSL Termination) is done mainly for performance reasons and to simplify backend infrastructure.

🔹 `Why Does Getting an HTTPS Response Consume More Energy?`
- TLS Encryption/Decryption is CPU-Intensive 🖥️
HTTPS (TLS) requires encrypting and decrypting data at both the client (browser) and the server (backend).
- If every backend pod has to decrypt incoming HTTPS traffic, it adds extra CPU load, which increases energy consumption.
- If the Load Balancer (ALB, NLB) handles decryption, backend servers don’t need to process SSL, improving efficiency.

💡 `Example:`</br>
A web server handling 10,000 HTTPS requests/sec must perform 10,000 SSL handshakes (costly).
If SSL is terminated at ALB, backend pods receive plain HTTP, reducing CPU load.

---
### **<span style="color:#B48EAD;">🔹 What Actually Happens When a User Requests HTTP (<a style="color:#B48EAD;" href="http://example.com">http://example.com</a>)**</span>
---

📌 `Case 1: HTTP-to-HTTPS Redirection (Your Current Setup)`

1. **User requests** `http://example.com` (**HTTP**).  
2. **The ALB receives the request on port 80**.  
3. **ALB sees the annotation:**
   ```yaml
   alb.ingress.kubernetes.io/actions.ssl-redirect: >-
     {"Type": "redirect", "RedirectConfig":{ "Protocol": "HTTPS", "Port": "443", "StatusCode": "HTTP_302"}}
    ```
4. **ALB sends back a `302 Redirect` response to the user.**  
5. **The user’s browser automatically retries the request over HTTPS (`https://example.com`).**  
6. **Now, the HTTPS request reaches ALB on port `443`, and ALB processes it normally.**  

> HTTP traffic never reaches the backend — it gets redirected to HTTPS first.

---

📌 `Case 2: ALB Only Listens on HTTPS (Forcing Secure Traffic)`

If ALB does **not** listen on port `80` at all, **HTTP requests fail immediately** instead of being redirected.

You can enforce this with:  

```yaml
alb.ingress.kubernetes.io/listen-ports: '[{"HTTPS": 443}]'
```
>  User must always start with https://—HTTP requests will fail.
---
📌 `Case 3: ALB Allows Both HTTP & HTTPS (No Redirect)`

If you **don’t enable HTTP-to-HTTPS redirection**, the ALB will **allow both HTTP and HTTPS traffic** to reach the backend.  

❌ **This is less secure** because some users may access [`http://example.com`](http://example.com) without encryption.  

---
## 🔹 What is TLS? (Transport Layer Security)
---

## 📌 `What is TLS?`

**`TLS (Transport Layer Security)** is a **cryptographic protocol`** that secures communication over a network by encrypting data between a client (browser, API, etc.) and a server.

- **`TLS is the successor to SSL` (Secure Sockets Layer)** and is **more secure & efficient** than older SSL versions.  
- **`TLS ensures:`**
    - **`Encryption`** 🔐 – Data is unreadable to attackers.  
    - **`Authentication`** 🛡 – Verifies that the server is who it claims to be.  
    - **`Data Integrity`** ✅ – Prevents data from being altered in transit.  

---

> ### 🔹 `Is TLS the Same as SSL?`
>       ✅ TLS (Transport Layer Security) is the successor to SSL (Secure Sockets Layer)
>       ✅ TLS is an improved and more secure version of SSL. 
>       ❌ SSL is now deprecated, and when people say "SSL," they often mean TLS

---

### 📌 `TLS vs. SSL – What’s the Difference?`

| **Feature**       | **TLS (Modern, Secure) ✅** | **SSL (Old, Deprecated) ❌** |
|-------------------|-------------------------|-------------------------|
| **Security Level** | High 🔒 | Weak (vulnerable to attacks) |
| **Latest Version** | **TLS 1.3 (2018)** | **SSL 3.0 (1996, obsolete)** |
| **Performance** | Faster & More Secure ⚡ | Slower & Less Secure |
| **Key Exchange** | Uses modern **ECDHE (Elliptic Curve Diffie-Hellman)** | Uses outdated **RSA key exchange** |
| **Recommended?** | ✅ Yes | ❌ No (All major browsers have removed support) |

📌 `TLS completely replaced SSL due to security flaws in SSL.`

---

