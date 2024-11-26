# -Ariadne

# Download and flash kernel for Pixel 7

1. Download the Pixel 7 Pro's kernel source codes
```shell
mkdir /pixel7-kernel
cd /pixel7-kernel
repo init -u https://android.googlesource.com/kernel/manifest -b android-gs-pantah-5.10-android14
repo sync
```

2. Go to the directory of the source code, then input 
```shell
rm -rf /pixel7-kernel/android-kernel/out/android13-gs-pixel-5.10/dist/* # clear previous generated files
# cloudripper is another codename for pixel 7.
# Change it to correct one for your pixel
BUILD_CONFIG=private/gs-google/build.config.cloudripper build/build.sh
```

3. Compiled files are generated and stroed in `/pixel7-kernel/out/android13-gs-pixel-5.10/dist/`, then we can flash them into the kernel
```shell
cd /pixel7-kernel/android-kernel/out/android13-gs-pixel-5.10/dist/

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

3. When modifying the source code of the kernel, only the codes stored in `private/gs_google` directory will work after flashing you custom kernel. Otherwise, you modifcation won't work.

4. You can refer to code dir `gs_google` of this repo and make changes correctly to build the kernel.


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
