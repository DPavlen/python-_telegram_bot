import logging

logger = logging.getLogger(__name__)


async def echo_handler(update, context):
    if update.message.text:
        text = \
            f"What does \"{update.message.text}\" mean?\nTry to type /help."

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text
        )


