# -Ariadne



# Collect Evaluation Results
First of all, please go to dir contained traces
```
cd AppTrace
```
## Coverage and Accuracy Results 

Run commands below to get our hot data prediction coverage and accuaray
```
./get_cov_acc.sh
```
The result will be in ```cov_acc_result.txt``` inside AppTrace dir.

## Replay Trace

You can replay our collected trace using
```
./replay_app_trace.sh
```

## Extract Other Evaluation Results 
```
./get_eva_result.sh
```
The result will be in ```final_result.txt``` inside AppTrace dir.
