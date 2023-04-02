import logging

from src.discord.discord_module import DiscordBot

if __name__ == '__main__':
    logging.info('Inizio esecuzione programma')
    try:

        DiscordBot().start_bot()
        pass
    except Exception as e:
        logging.error(f'Errore durante l\'esecuzione del programma: {e}')
    finally:
        logging.info('Fine esecuzione programma')
