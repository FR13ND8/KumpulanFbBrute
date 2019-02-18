clear
bi='\033[34;1m' #biru
i='\033[32;1m' #ijo
pur='\033[35;1m' #purple
cy='\033[36;1m' #cyan
me='\033[31;1m' #merah
pu='\033[37;1m' #putih
ku='\033[33;1m' #kuning
echo
echo
echo $ku"|---------------------------|"
echo $ku"|"$pu" Penyusun : Riski Darmawan"$ku" |"
echo $ku"|"$pu" Kumpulan : BruteForce Fb"$ku"  |"
echo $ku"|---------------------------|"
echo $i"#############################"
echo
echo $me"()===||======================>>"
echo $pu"[1] Brute Force Fb MRA27"
echo $pu"[2] Brute Force Fb PHP"
echo $pu"[3] Brute Force Fb BR1G4D3"
echo $pu"[4] Brute Force Fb Iqbalz"
echo $pu"[5] Brute Force Fb N1ght420"
echo $pu"[6] Brute Force Fb MBF"
echo $pu"[7] EXIT PROGRAM"
echo $me"()===||======================>>"$pu
read -p"     [?] Pilih No : " pil

if [ $pil = 2 ];then
clear
figlet -f slant "W A I T"|lolcat
sleep 1
git clone https://github.com/MRA27/FBNEW
cd FBNEW
python2 MRA27.py
fi

if [ $pil = 1 ];then
clear
figlet -f slant "W A I T"|lolcat
sleep 1
git clone https://github.com/FR13ND8/fbbrute
cd fbbrute
php fb.php
fi

if [ $pil = 3 ];then
clear
figlet -f slant "W A I T"|lolcat
sleep 1
git clone https://github.com/FR13ND8/Fb-Cracker-v.3
cd Fb-Cracker-v.3
python2 crack.py
fi

if [ $pil = 4 ];then
clear
figlet -f slant "W A I T"|lolcat
sleep 1
git clone https://github.com/IqbalzNoobs/fb-brute
cd fb-brute
python2 brute.py
fi

if [ $pil = 5 ];then
clear
figlet -f slant "W A I T"|lolcat
sleep 1
git clone https://github.com/N1ght420/FaceBrute
cd FaceBrute
python fb.py
fi

if [ $pil = 6 ];then
clear
figlet -f slant "W A I T"|lolcat
sleep 1
git clone https://github.com/FR13ND8/mbf
cd mbf
python2 MBF.py
fi

if [ $pil = 7 ];then
echo
echo $cy" TERIMA KASIH SUDAH PAKAI TOLS INI"
sleep 1
exit
fi
