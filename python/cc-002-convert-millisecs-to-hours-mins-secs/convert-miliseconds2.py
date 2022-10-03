  while True:
  print("Bu program milisaniyeyi saate, dakikaya ve saniyeye çevirir. Çıkmak için 'exit' yazın.")
  sayı = input("Lütfen milisaniye girin (sıfırdan büyük olmalı): ").lower().replace(" ", "")

  if sayı == "exit": 
    print("Programdan çıkılıyor, hoşça kalın.")
    break

  elif (not sayı.isdigit()) or (int(sayı) < 1):
    print("Geçersiz giriş !!!")

  elif int(sayı) < 1000:
    print(f"Sadece {int(sayı)} milisaniye. ")
    break

  else:
    saniye = int((int(sayı) / 1000) % 60)
    dakika = int((int(sayı) / (1000 * 60)) % 60)
    saat = int((int(sayı) / (1000 * 60 * 60)) % 24)

    if saat < 1 and saniye < 1:
      print(f"{dakika} dakika")
      break
    
    elif saat < 1 and dakika < 1:
      print(f"{saniye} saniye")
      break

    elif dakika < 1 and saniye < 1:
      print(f"{saat} saat")
      break

    elif saat < 1:
      print(f"{dakika} dakika {saniye} saniye")
      break

    else:
      print(f"{saat} saat {dakika} dakika {saniye} saniye")
      break
