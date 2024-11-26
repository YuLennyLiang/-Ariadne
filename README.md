# -Ariadne

# This markdown introduces how to download and flash kernel for Pixel 7

1. Download the Pixel 7 Pro's kernel source codes
```shell
repo init -u https://android.googlesource.com/kernel/manifest -b android-gs-pantah-5.10-android14
repo sync
```

2. Go to the directory of the source code, then input 
```shell
rm -rf /mnt/Pixel7/android-kernel/out/mixed/dist/* # clear previous generated files
BUILD_AOSP_KERNEL=1 SKIP_MRPROPER=1 ./build_cloudripper.sh       # cloud ripper indicates Pixel 7 Pro
```

3. Compiled files are generated and stroed in `/home/hubery/mywork/pollor/pixel7-kernel/out/mixed/dist/`, then we can flash them into the kernel
```shell
cd /mnt/Pixel7/android-kernel/out/mixed/dist/

adb reboot bootloader
fastboot oem disable-verification
# fastboot -w # this command will wipe the device, use it when needed

fastboot flash boot boot.img
fastboot flash dtbo dtbo.img
fastboot flash vendor_kernel_boot vendor_kernel_boot.img

fastboot reboot fastboot

fastboot flash vendor_dlkm vendor_dlkm.img
fastboot flash system_dlkm system_dlkm.img


fastboot reboot
```

3. When modifying the source code of the kernel, only the codes stored in `aosp` directory will work after flashing you custom kernel. Otherwise, you modifcation won't work.




# Collect Evaluation Results
First of all, please go to dir contained traces.
```
cd AppTrace
```
## Coverage and Accuracy Results 

Run commands below to get our hot data prediction coverage and accuaray.
```
./get_cov_acc.sh
```
The result will be in ```cov_acc_result.txt``` inside AppTrace dir.

## Replay Trace

You can replay our collected trace on smart phone using
```
./replay_app_trace.sh
```
This will generate evaluaiton result which is collected on real smart phone.

## Extract Evaluation Results 
```
./get_eva_result.sh
```
The result will be in ```final_result.txt``` inside AppTrace dir.
