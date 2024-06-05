import os
import telebot

# My name is VLAD_M_TELEGRAM_BOT_1_TOKEN
token = os.environ['VLAD_M_TELEGRAM_BOT_1_TOKEN']
bot = telebot.TeleBot(token, parse_mode='MarkdownV2')

msg = r"""
*bold \*text*
_italic \*text_
__underline__
~strikethrough~
||spoiler||
*bold _italic bold ~italic bold strikethrough ||italic bold strikethrough spoiler||~ __underline italic bold___ bold*
[inline URL](http://www.example.com/)
[inline mention of a user](tg://user?id=123456789)
![👍](tg://emoji?id=5368324170671202286)
`inline fixed-width code`
```
pre-formatted fixed-width code block
```
```python
lst = [1, 2, 3]
for x in lst:
    print(x)
```
>Block quotation started
>Block quotation continued
>Block quotation continued
>Block quotation continued
>The last line of the block quotation
**>The expandable block quotation started right after the previous block quotation
>It is separated from the previous block quotation by an empty bold entity
>Expandable block quotation continued
>Hidden by default part of the expandable block quotation started
>Expandable block quotation continued
>The last line of the expandable block quotation with the expandability mark||"""
@bot.message_handler(commands=['start'])
def command_start(message):
    text = str(message)
    bot.send_message(message.chat.id,
                     msg)


if __name__ == '__main__':
    bot.infinity_polling()
