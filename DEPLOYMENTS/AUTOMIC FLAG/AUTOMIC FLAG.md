## `AUTOMIC FLAG`

⚛️ `What --atomic Does?`
- If the Helm upgrade or install fails for any reason:
- All created resources (Deployments, Services, ConfigMaps, etc.) are automatically deleted.
- The Helm release is rolled back to the previous stable version.
- Users can avoid the deployment being left with half-applied or broken resources in your cluster.

🔁 `When Does It Roll Back?`
If any of these fail:
- Pods don’t become Ready within the timeout.
- Health/liveness/readiness probes fail.
- Any template renders badly.
- Any resource creation fails (e.g., quota exceeded, bad image, etc.)

✅ **Helm waits for success thanks to --wait, and if it doesn’t succeed within the timeout, --atomic kicks in to clean up.**

--- 

🧨 `Without --atomic (and with --wait):`
If the deployment fails:
- Resources stay in the cluster.
- You must manually investigate, fix or rollback.
- Helm marks the release as FAILED, but leaves you with a broken app.

Command:
```
helm upgrade \
  ${INPUT_HELM_RELEASE_NAME} \
  main/${INPUT_HELM_CHART_NAME} \
  --install --wait --atomic ${FLAG_DRY_RUN} ${FLAG_DEBUG} \
  --timeout ${INPUT_TIMEOUT} \
  --history-max ${INPUT_HELM_HISTORY_MAX} \
  --namespace ${INPUT_EKS_NAMESPACE} \
  --description "${INPUT_HELM_DESCRIPTION}" \
  -f ${VALUES_CLUSTER} \
  -f values-file.yml \
  -f values-inline.yml \
  -f values-pod-labels.yml \
  --version ${INPUT_HELM_CHART_VERSION}
```

`Variable / Flag`	Purpose`

| **Variable / Flag**       | **Purpose ✅** | 
|-------------------|-------------------------|
| --dry-run | Simulates the upgrade without applying changes |
| --debug | Prints verbose debug output |
| --timeout | How long to wait for resources to be ready| 
| --atomic | Rollback if anything fails |
| --history-max | Keep only the latest N release versions |
| --namespace | Kubernetes namespace to deploy to |
| --install | Install if release doesn’t exist |
| --wait| Wait for all resources to be healthy before considering the deployment successful |

