from typing import TextIO

import requests
import json

cookies = {
    '_pk_ref.1.8bab': '%5B%22%22%2C%22%22%2C1731492822%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D',
    '_pk_id.1.8bab': 'd9f2aad2dbc29785.1731492822.',
    '_pk_ses.1.8bab': '1',
    'ZiraatCookie': '!e/0MfhWt/60oQnsSM6AtY/LsgU/QmDKjYRFFc5esoEKl9yEm2kdwjVh9b99nQT67/lPNkMAMUlRBRtk=',
    'ziraat': 'r41vosqdu5hjde25ypz2e2zc',
    'customerType': 'rtl',
    'rdLng': 'TR',
    'TS01ce8ee3': '013aabc898abe25f0aaab920c6cfe811bb81a87dd75e43894f201a39922ec3f2eeb59b17d72bf1753444d133fb6118da198cdfd9c1aa600a040ea0e5bf57ef592a70e0803a0747dca8fe60f3aa9a1ec2015f42f6deb72bc938a0deb1ffff2959dde3b2e92f8df8e9e7924be4e14bad5d8dc85d0943bd3e8e3d391479f51b2b5c2d5653394f3bb0d9e144e438fa81e32ac42e0a7892659881fa7d29b13f13e34653928dab3f029cfc2223ec131c8b77535f0b637f01',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': '_pk_ref.1.8bab=%5B%22%22%2C%22%22%2C1731492822%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_id.1.8bab=d9f2aad2dbc29785.1731492822.; _pk_ses.1.8bab=1; ZiraatCookie=!e/0MfhWt/60oQnsSM6AtY/LsgU/QmDKjYRFFc5esoEKl9yEm2kdwjVh9b99nQT67/lPNkMAMUlRBRtk=; ziraat=r41vosqdu5hjde25ypz2e2zc; customerType=rtl; rdLng=TR; TS01ce8ee3=013aabc898abe25f0aaab920c6cfe811bb81a87dd75e43894f201a39922ec3f2eeb59b17d72bf1753444d133fb6118da198cdfd9c1aa600a040ea0e5bf57ef592a70e0803a0747dca8fe60f3aa9a1ec2015f42f6deb72bc938a0deb1ffff2959dde3b2e92f8df8e9e7924be4e14bad5d8dc85d0943bd3e8e3d391479f51b2b5c2d5653394f3bb0d9e144e438fa81e32ac42e0a7892659881fa7d29b13f13e34653928dab3f029cfc2223ec131c8b77535f0b637f01',
    'Origin': 'https://bireysel.ziraatbank.com.tr',
    'Referer': 'https://instagram.com/login',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

data = {
    '__EVENTTARGET': 'ctl00$c$RetailLoginButton',
    '__EVENTARGUMENT': '',
    '__VSTATE': 'xU5G9WJln7BUrtZRmd5NV0IqKVd3F3IjHnej6zHExTy48dMAXSJrrsCsmaZoGlxeWFk0DfAVSOsBbZnJgBxgqoAFy9wHXdYxq0eg38Nd/oco4gWGd5Q9hOgD02dyCyqw9yL7BnVGDW5UFpYAbUNlUBAtFSvYwTTdmsRT9JYNgWth4K51ucqKYjmn53dL7OnC3TzpzZZHTRCMS+WexMb432k3cGCY56FP0SnlVaWJn6UcjCaNN7G2GH1Ax0iO6sKMKHmjmPjcEIPtOPRKNCP6sAFoHbRfxU0zB1YIkqfwrssRy8bQL61nU0BvP5JJG+VyowYes2aOVB+KO/eM/XFDctIZJ0ZzbAt+eiJnuAfYlrBkMFlTurRRY4D/YB+YW45CpK/KNCSaA03tQbjog5sR3vW2VsBabTNXY5Xy0VIrzy6/2Gc80UPhKaucymV+u8oP1bq6Gr/bKDS1r+1GADgf/vvyAnp+WK0boB0J68jmgSWlRegtff9G25YIwx7YL2dHZrNLfyQCDtrjcQFoMkHSfFsg/VYTSzZ7jTjPgdMlALXOSJWyH8gUSBjTyBCbVnd6m44BokP0pmjYlMeVP2bHh86mNvCTZfcVdMJL7X+d5Mgm5cAuVV1tqaaAOTHBvSVuzXID2H/PHgbxT/qgIi0Ygc0kGgxgNFNIB7xG5iYcur3leHdbIYIEfcoO3I+OR6hPRhn2ln5Rl6pbu1gNZ1CflcJkt/dnNQxyNs9shy9EO/fPygw9HpTD0RDN2i3rGjCypU9Ys8PvgUGa61dop4ibzzTfeYlIvu0Kgd/Fyy1x8ZrDnF/l5eTI4Q5j3oYXhsewUeok6DS4wAXuoruPgZco/1/NPi7pPWq3lTfFL+GcNBcVExTApBmo+EqeG25IVdqR/xqNNCdn4S4vw1mAUyDyVuT+RUj7zqBQD39XVx0SNYF1jySGTugR3C1tOpHPKLcFCT4EyBh2qkPeLZkyC7UHkltA/X+FZk9IxWuu6u8Sr7uObjmZL5UdU6HPwikYOv890LJ6aaxxxS3QL7G5MLXsBRZCLmPTyBv7gk112vxfzj4A3ZfHm8NTsZs5tUUwPBBIFcV7DbSQdTt+lXsDaghzMuBrY4EZn4CN22Ibnd+7RSYHnosTTK+dex12w6BDN9QhVF5PEL+fW0Za+kDAazOPOdAzEWXJXR0NzlPUdOy0mcK08UJTIGwobujw9jkfwBsOwsaMRCjfZRVV0H6y0YD/8x6CMbdUGGVoz0yx2rLRavZxpfQGikmKQXG8E7SFdluQlwx+hF4Mhx47kAxmCyJFv+vQdQJ1tjQApaRecNiJL02n6VZK66IACTzJfZL6VTLkNABCy55zl2zBggJ14OUv13Y6YtR1apsS83JtgACkr5iuH3iv0ut3kJYEvARj73Kl9ant13VvepslMiCJnbmWF6p2ed7UhubuCltZ420Xm0PRVacnhxLU/k28Enbd9Uc3e85xdE0eyABGN8zve3wscULcuGjRZe9NuaOCSEwEyfeN7Ueoa066kZ0uO9Q1XBEldVz+pbDomjH3GSd7osx4JsDHKl+eH2wtKbj3N37L8A1JINOopaNeg5Dki2h/ssakdOgraUdFzmpQ0MaGXmvTqMwTnsXbSUywCqN+FCVbbb1rDuTwbrVcFalpGsyjftw4Tda5W7Ytiu98PbOi6p34CUtDYHiEtCGgBftdqHZB6AADcRivp7evVc0FdsgA2RAwO+et5oZOTzhAsTWIYfyYxEha41EF+55tgLKW42kSPjs=',
    '__VIEWSTATE': '',
    '__VIEWSTATEENCRYPTED': '',
    '__EVENTVALIDATION': 'JmdNrihJiQ1fwSu39Co2qJXvZlJYzE/Rk6PDdfZxTyFwJByrfZNse1slEBMO1zdtZbIAd734bIG56aTaOuocrfgsCiCIWF7ZpKPdWW8i8AMRyLB4V0qv4albX2p9j/WR++B9pC22ArzanHGqfYkxw3Kn8JKftrfHqqOSK5OX6OjV6LaLedr1AA/2mbjRpgLCbpOi1YYj1cmp/2sPokhhnR/1R/Ko3F3VpLsGSvt2KGiq+4JNXisXr8gN1+snhJkkI8GADSO/SiTjAGEFUXMQ71ouycaBEcMOu3ZmPiRQQwwOzrWkUKYJpegHOEZZ+nhcdc01h4xJskJt1kgfq5TY3MkssWO6ah1srvA4brZeh58aqF55ca/+b+Okkju4//mEirTVMF/siYSMswMzzprL5bkvWAwCCfAepugP7QuqWmbsJk20L7Q6UJshQB0wrvtwgYRZELMiRmiJ9EqptRs22kD49BdI8rydUMtxuWEjEhmumjpJS43htLh19xU6OUbWsYu7rWMwsCZ02uq8N2X/xPqfWRCTSinShDtrOL0hqSQa5r4HP44dQpthmLlvw6l/9HgXNQzVe2kfaB3QCUb960y7Y7nwvPDqupb8AyI6Fq7yFMij0bTuBPlga2X2IDl/FUBTn9yvGfGfpM2z0dKabnuC0QMB8dT/0cuwjAwpgoWImDtKaGn1NMGKbfOYQUYFf490jjoEHq98H5u5MphJQRtHTJltV76pu6tRbBbdocqxjKecKFt688MnN36S1IjqvrXBMgrDE+sHnh86jmUihh2pTtxSlBHVdxF57a7quu1oKGrue2n0/N3pI658mPfRuODy59DkFKMSUULUtYgptj9SgOjYTrr0NQEi0Z+i4pH3qy3trwYVymt7aFBARWLFFJKvIWC3xEpI/T6UBisUi7Rw7MBFQoRt9nG/u5nJo+CTf6szKwtP/O3/FNcfAJfEiJp0Flw87fbR1Avjm5q5fA6raYF7/14IV6yc27lpdUf1kfzLrFuh6nt3TeWgP+fwvpSGknEOx4xQZIScx+8Bx8i5mhm9k4rAuAIc/9dyfT2tqvtMSlSiMO4ZSQLaF3dUhKJbGU9NzxNCnP25zYgAAcxyA6O+VJnDAXburg==',
    'ctl00$TabInstanceUniqueKey': '',
    'ctl00$NavigationHiddenInput': '',
    'ctl00$HdnClientParametersCacheKey': '96b6ec6ba2fd4173980fd61028371662',
    'ctl00$HdnCurrentCulture': 'tr',
    'ctl00$HiddenIsIOSDevice': 'True',
    'ctl00$HdnBaseUrl': '//bireysel.ziraatbank.com.tr',
    'ctl00$zrt_user_prefs': 'k0a44j1eJNlY5BSo9z4ofjb75PaK4Vpjt1szHVXU3vtnTDovmkXTGYz3ccbbJYMLgiPFU77qZoOSix5ezdstlYysrhsui64J5rQhyWesjEPm8LKfAaZ4pAJZ7OQuyPBB2SE0fYx92yITehu_jftckcKyAd65hz7M6uJ3IsbUDQlqbTL3ImBUs_43wuZPup_nH2t05oaYAhrcpMxE6DBUr5xj6KkseVqvSjoCM4tvLG9mhORoVj.rVaopxUC55fqQsygwGnMxawgc9jAjfstpBSLR2SxUC56MnGWpwoNSUC53ZXnN87gq1md96gffpJJjPuQkmqkOeLaxGMuJjkWibgazLK7lrHLy.jKY.MekKCaMCJ9VyKAwcMtipp0ibgazLKCq7GY5BNv_1BNlY0bqhs5AXnZvStJyyNpjeWJ6mkjmWUdCzI5a5BhpFg46R3eFmp48k0e.mk02DAVekVbNDSFmWAJbIw3gzilT3NQdL9.HGOti4yzGMEisdV9CiWnuxKXVPgZ60_dyA3nt8I8.hWrUGOKiJ64XVA4.L9.gJ14Nc1gtIA4.A2p9gJ0FH1lFCUC68mlFCUC68mlF3xZf4.IqHgJ.hi4Nc32T1QIQc5xrDz.ICQiSulF1kteHQB0Rp52yz4a1xU..D5k',
    'ctl00$user_prefs2': 'rO0ABXNyACdjb20udGhlNDEuY29tbW9ucy5jcnlwdG8uQ3J5cHRvRW52ZWxvcGUAAJbgqPhc8wIAA0wABWFsaWFzdAASTGphdmEvbGFuZy9TdHJpbmc7WwAMZW5jcnlwdGVkS2V5dAACW0JbABBlbmNyeXB0ZWRQYXlsb2FkcQB-AAJ4cHQABGhkaW11cgACW0Ks8xf4BghU4AIAAHhwAAACABvcfmUz_Ey2zG-5ota-DOsmXz-HOEkBkmZK890Co8T-XBCEQjw3cZWLWYTWChAWHvHcTIyen-Pi-XI7cTE1PV2rFNYSa5aqNGSTkJ-GTm5-8e76HnIiSnJBSt82WkB5eSAPm0nZoNot6AxHOki6spRZMwhOc0m0pdA0a0w3liB-uGUKOLWCliZvdk-x95HY1jRykesMl9dWRyHJFkbChkhCOoFmO92VWjJ3oX6SVhOAW55SQjayUcEe4TP2qbWJH2dmrABgVEAPHMyuJHFiMiZfkPNE8Vou8jZ_-I9cHdQAf2mFx9-V6ISfckj_3lU0pY7zUqYDa-btA0hRjDEu4CfUBe8EUZdeTrVV8qwmq3DsGdfXDnIluW08Of_P5Dyt4BoKAFNS0F13sPb8PGMUc_Kv2SjE1-lKJ7SYBKscGfjIgShQMwym5uXR30VYgwEQDr6UZGaF0_I2obOADyYU8HIFw8xKv647So4rsB2JN77CJCp1SJsIoMXglhZI26KpqRlYyVt04ZqF3UKRPKSHhpNt9o8aBdICSTBAEquJDKQPqvYWHZIPoUu961Bpb-Eq1sDRN8Z12acJceKPoUFPDsBhtGEmv7ms0ojRg9Mq_3_hppGyRSh7oMzcOea-MBDcQ_-HzrhX9Yf5Htk9lHmBIbH5vnd93MBZqaN_bnipr8zgdXEAfgAFAAADkI_g8JkNBilAFZXkqc0FHFnRgUcE27LfSUO9F5jgqiwCORogE33ZFGU534oD6TO1QgISo9JgcXxDYOLSMZUVGbDLCUhJ86r1H3S_diD9PmGrGdYD5NlR9JhFMY4rjsNrif80dy_VI50mbYt8aD8pVjq0WOJWXQ_CV5w2VnwAK_0s7BWVrsrTZIzuhZ3HB884cvIsrF7LYL9RB7KMjMrH228wENxuEITV2R-OJwXG92BTQWoUdEYhE6ntE4nQBXOwyyhcXe90RBlFsHfY6VVmo79lAK85CjNe6jbFLM1agz8RPPTpQ7SpNoZIjQTxfMhJsvCcQAzNHEYPH0ix-fT-kxmzdXaiq7zfa0I5-Lb8ngA7MidqFk8S1nf1QU5r7XbuTyoJBHnLsmJspG_05ZZZbZzxzIYFxdx28z2PCEMCTp3Zjcq7KM2zIVW5cnZR3-RjweL7V0Q_yrIJEBWyDj19ubPdv4zJ7Rjr9U1iNDF4Y6lBTb_flU5kTcwn7gYO6VLfUopbC-YlSymHb-qVsAwMar4nCKr4M1r5YhCfpfgUM-krX6bmdJOQO_03UpR6yE1kU_Z1Nddco99IEaQxNfLCMnaJdrV7DQCR_CciABP2jW9gjYxgV7iSHzVWSnEd2hUu3vJn3wg8Gu0vGQCupPJMTv_kZvzK8uKzZ7FUtoEobl8D0sUr_jP_DLBTWMLj4u_8Vanjyt02a7lQRwjE7Nfco9OsbRtcOIS4JyrBsPgg4R1rNQjahs219lpk4JyAOpMXyuX_3haOpx05YmrcwkzuRdYxOOwviNiv8LntRQrfoafeZ0SqJjo-QBCZIby-5IBn7wOVlH1-SEhCg-CbWuK6FN0sP9oGZ2MaSTl-qae5f5UK0CrGjkREJqXzTmEsYfb2mo6NN8p3ei8CTH8VvFDABJO9naF7VY1B-b5CDtyJUqT-YG3Zu2zX5cgmFOnuBOz3MJ7rr9mtJpLebkBksFqMJprWTGLzseNu6Xt14NtZyVwA8oDG7cWzRh-ZO6Zn7whO0KM5Ui9P5TD48J5_T048fWbmBRGmknVLD1Fzf7OQxfASnOjrZqKZFGWZr0AuEmq4u-yxd2eTTdoPBz-ptcUcuAxP64Pm_jer0CW6FEwq6Lba9Qyl0WLGOwM8_mpchSqtW-17gFs3TMn84CiucKEojH12wY93SdClmMs1KVft1ze8M7yJG1240uwwm_ASarICRw',
    'rdLng': '',
    'ctl00$c$CookieEditStatusField': 'false',
    'ctl00$c$RetailIdentityTextBox': '',
    'ctl00$c$RetailIdentityTextBoxdd5fcb6461304a': '3190ee44f70059bce136bf10c33c4ecea5ec236a2bb4679ffa19ae963aadfe3f1abf65eecfce5949285716b0ee243661dca08bfee3f4dd66bca379cde9656e264927c5f740d3e47fe92fcb1d28bd72e16407aa399848fea96663e4961a5deac5bf9b1afb5239d0c74c0040372e08262ad7b05971c68219688f9dbf359985567d',
    'ctl00$c$RetailPinTextBox': '',
    'ctl00$c$RetailPinTextBoxdd5fcb6461304a': '17107db9c4db67feb59d095e1eed8b4fca6a899ecc007b05b540152af72ed5c0af05779f60a7f5b0a4e5dc80d9555f3e4406aacc5159dd7a1a48099a0f4721c81f9a69c67cf4cf6df9613b42dfca5dfe66400827ed942cb79f9cfef7423ea5dec65783170291ee894880197400514ab757cf7c85558703f80759b6630adb91d8',
    'ctl00$c$CorporateIdentityTextBox': '',
    'ctl00$c$CorporateIdentityTextBoxdd5fcb6461304a': '',
    'ctl00$c$CorporatePinTextBox': '',
    'ctl00$c$CorporatePinTextBoxdd5fcb6461304a': '',
    'ctl00$c$CorporateUserNameTextBox': '',
    'ctl00$c$CorporateUserNameTextBoxdd5fcb6461304a': '',
    'ctl00$c$HiddenField1': '29',
    'ctl00$c$HdnSpiderToken': '',
}

response = requests.post(
    'https://instagram.com/login',
    cookies=cookies,
    headers=headers,
    data=data,
)


# Çerezleri bir dosyaya kaydet
file: TextIO
with open('cookies.json', 'w') as file:
    json.dump(cookies, file)
print("Çerezler kaydedildi.")
