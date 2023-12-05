kubectl get pods --all-namespaces --field-selector=status.phase=Running -o wide | Out-File -FilePath "running_pods_list.txt" -Force
Write-Output "DONE"