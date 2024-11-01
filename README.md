# BerogovPyCAI

**BerogovPyCAI** -  это неофициальное API Character.AI. Это измённая билиблиотека PyCharacterAI. Данная библиотека не использует `curl_cffi`. Библиотека предназначена для упрощения взаимодействия с Character.AI.

## Установка

Сначала убедитесь, что у вас установлен Python версии 3.7 или выше. Затем установите необходимые зависимости с помощью pip:

```bash
pip install httpx aiohttp
```

## Пример Использования

```python
import asyncio

from BerogovPyCAI import get_client
from BerogovPyCAI.exceptions import SessionClosedError

token = "TOKEN"
character_id = "ID"


async def main():
    client = await get_client(token=token)

    me = await client.account.fetch_me()
    print(f"Authenticated as @{me.username}")

    chat, greeting_message = await client.chat.create_chat(character_id)

    print(f"{greeting_message.author_name}: {greeting_message.get_primary_candidate().text}")

    try:
        while True:
            # NOTE: input() is blocking function!
            message = input(f"[{me.name}]: ")

            answer = await client.chat.send_message(character_id, chat.chat_id, message)
            print(f"[{answer.author_name}]: {answer.get_primary_candidate().text}")

    except SessionClosedError:
        print("session closed. Bye!")

    finally:
        # Don't forget to explicitly close the session
        await client.close_session()

asyncio.run(main())
```



## Лицензия

Этот проект лицензируется в соответствии с лицензией MIT. Пожалуйста, смотрите файл [LICENSE](LICENSE) для более подробной информации.

## Контакты

Если у вас есть вопросы, предложения или обратная связь, не стесняйтесь обращаться по [dev.berogov@gmail.com] или Telegram: @Berogov.
