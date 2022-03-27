ORIGIN = "LMDE 4 'Debbie'"
ORIGIN_CODENAME = "debbie"
ORIGIN_BASE_CODENAME = "buster"

DESTINATION = "LMDE 5 'Elsie'"
DESTINATION_CODENAME = "elsie"
DESTINATION_BASE_CODENAME = "bullseye"

SUPPORTED_EDITIONS = ["cinnamon"]

CHECK_ABSENT = ["ippusbxd"]

CHECK_PRESENT = ["default-jre", "os-prober"]
CHECK_UP_TO_DATE = ["mintupgrade", "apt", "dpkg", "linuxmint-keyring", "ubuntu-keyring", "mintsystem"]

PACKAGES_PRE_REMOVALS = []

PACKAGES_REMOVALS = [
    "tomboy",
    "libxplayer-plparser18",
    "xplayer-common",
    "gksu",
    "memtest86+",
    "*hwe-18.04*",
    "linux-hwe*",
    "python3-tinycss", #
    "indicator-application",
    "grub2-theme-mint"
]

PACKAGES_ADDITIONS = [
    "neofetch",
    "ffmpegthumbnailer",
    "amd64-microcode",
    "intel-microcode",
    "celluloid",
    "drawing",
    "gnote",
    "adwaita-icon-theme-full", # 19.3->20
    "warpinator", #
    "alsa-topology-conf", #
    "alsa-ucm-conf", #
    "mesa-vdpau-drivers", #
    "mesa-vulkan-drivers", #
    "cryptsetup-initramfs",
    "cryptsetup-run",
    "libreoffice-gtk3",
    "gamemode"
]

IMPORTANT_PACKAGES = [
    "mint-meta-cinnamon",
    "mint-meta-mate",
    "mint-meta-xfce",
    "xreader",
    "xed",
    "xviewer",
    "pix",
    "mintsystem",
    "metacity",
    "nemo-preview",
    "mintdrivers",
    "mintupdate",
    "mintsources",
    "mintinstall"
]