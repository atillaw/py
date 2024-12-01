#-+-+-+-+@KringofTool-+-+-+-+
#-+-+-+-+@KringofArsiv-+-+-+-+
#-+-+-+-+@KringofArsiv2-+-+-+-+
import os
from pyrogram import Client, filters


API_ID = "API ID'Nİ GİR"  
API_HASH = "API HASH'İNİ GİR"  
PHONE_NUMBER = "TELEFON NUMARANI GİR"  


ADMIN_ID = 'HESAP ID GİR' 


app = Client('KringofBABBA', api_id=API_ID, api_hash=API_HASH, phone_number=PHONE_NUMBER)


@app.on_message(filters.command("kopyala", prefixes=".") & filters.reply)
async def soloclone(client, message):
  
    if message.from_user.id != ADMIN_ID:
        await message.reply("Aynen bak oldu şimdi")
        return

    
    replied_user = message.reply_to_message.from_user

    if not replied_user:
        await message.reply("**Lütfen bir kullanıcıya yanıtlayarak komutu kullanın.**\n\n**Kullanım:** `.kopyala`")
        return


    first_name = replied_user.first_name
    last_name = replied_user.last_name if replied_user.last_name else ""
    bio = (await client.get_chat(replied_user.id)).bio or ""  #

    
    save_directory = "eski_fotolar"
    os.makedirs(save_directory, exist_ok=True)  

    current_photos = client.get_chat_photos("me") 
    photo_ids = []
    saved_photos_count = 0

    async for photo in current_photos:
        photo_ids.append(photo.file_id)
        file_path = await client.download_media(photo.file_id, file_name=f"{save_directory}/photo_{saved_photos_count}.jpg")
        saved_photos_count += 1

    if photo_ids:
        await client.delete_profile_photos(photo_ids)  
        
    photos = [photo async for photo in client.get_chat_photos(replied_user.id)]
    cloned_photos_count = 0

    for photo in reversed(photos): 
    
        file_path = await client.download_media(photo.file_id)   
        await client.set_profile_photo(photo=file_path)  
        os.remove(file_path)  
        cloned_photos_count += 1  
    if cloned_photos_count == 0:
        await message.reply("❌ **Kullanıcının profil fotoğrafı bulunamadı. Mevcut fotoğraflar silindi.**")
        return

    
    await client.update_profile(first_name=first_name, last_name=last_name, bio=bio)

    if bio == "":
        await message.reply(
            f"`İşlem Başarıyla Tamamlandı`\n\n"
          
        )
    else:
        await message.reply(
            f"`İşlem Tamamlandı`\n\n"
        )


app.run()