# How to Connect to a Running Container

To connect to a running container and execute commands inside it, you use the `docker exec` command.

---

## Why `-it`?

Every container is essentially running a **Linux environment** where processes communicate through three main channels:

- **`stdin`**: Input channel, where you send input to the process.
- **`stdout`**: Output channel, where the process sends its standard output (what we see on the screen).
- **`stderr`**: Error channel, where the process sends error messages.

The **`-it`** flag in `docker exec -it <container-id> <command>` is shorthand for `-i` and `-t`:

- **`-i` (interactive)**: Keeps the standard input (`stdin`) open and allows you to interact with the process. Without `-i`, any commands you enter will not be sent to the process.
- **`-t` (pseudo-TTY)**: Allocates a pseudo-terminal, which allows the output to be formatted properly, just like in a normal terminal. Without `-t`, the output may appear as raw text without any formatting.

---

## What Happens Without `-t`?

- Without the `-t` flag, you'll still see output from the process, but you won't have formatted output or an interactive prompt.
- For example, running `redis-cli` without `-t` may not display the formatted, interactive prompt you're used to.