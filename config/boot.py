"""
boot.py
This file is responsible for setting up and running a Flask app and a Discord bot concurrently.

To customize the Flask app:
- Set the FLASK_HOST environment variable to specify the host address.
- Set the FLASK_PORT environment variable to specify the port number.
- Place your HTML templates in the '../resources/views' folder.
- Create routes in the 'routes/web.py' file.
- Create API routes in the 'routes/api.py' file.                

To customize the Discord bot:
- Set the DISCORD_BOT_TOKEN environment variable to specify the bot token.
- Set the DISCORD_PREFIX environment variable to specify the bot's command prefix.
- Create commands in the 'app/Commands/Context' and 'app/Commands/Slash' folders.

To add more threads/parallel tasks:
- Create additional functions for each task you want to run concurrently.
- Create new threads using the threading. Thread class and target the respective functions.
- Start the threads using the start() method.
- Join the threads to the main thread using the join() method.
- For more information, refer to the Python threading documentation: https://docs.python.org/3/library/threading.html

GitHub URL: https://github.com/mahedizaber51/mvc-python
Author: Md Mahedi Zaman Zaber (mahedizaber51)
"""

import os
import sys
import threading
from flask import Flask
import disnake as discord
import glob
from disnake.ext import commands
import glob
# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

flask_enabled = os.environ.get('FLASK_HOST') # Check if the FLASK_HOST environment variable is set
discord_enabled = os.environ.get('DISCORD_TOKEN') # Check if the DISCORD_BOT_TOKEN environment variable is set

# Flask app setup
if flask_enabled:
    print("Flask app enabled")
    app = Flask(__name__, template_folder='../resources/views') # Define the Flask app
    with app.app_context():
        import routes.web # Import Web routes
        from routes.api import api # Import API routes
        app.register_blueprint(api) # Register the API blueprint

    def run_flask():
        app.run(host=os.environ.get('FLASK_HOST'), port=os.environ.get('FLASK_PORT'))

# Discord bot setup
if discord_enabled:
    print("Discord bot enabled")
    intents = discord.Intents.all() # Define the bot's intents
    bot = commands.Bot(command_prefix=os.environ.get('DISCORD_PREFIX','!'), intents=intents,)

    @bot.event
    async def on_ready():
        print(f'Logged in as {bot.user}') # Print the bot's username when it's ready

    def load_cogs(bot):
        cog_directories = ['app/Commands/Context', 'app/Commands/Slash'] 
        for directory in cog_directories:
            for filename in glob.glob(f'{directory}/*.py'):
                if filename.endswith('.py'):
                    cog = filename.replace('/', '.').replace('\\', '.').replace('.py', '')
                    try:
                        bot.load_extension(cog)
                        print(f'Loaded cog: {cog}') # Print the name of the cog that was loaded
                    except Exception as e:
                        print(f'Failed to load cog {cog}: {e}') # Print the name of the cog that failed to load

    def run_discord_bot():
        try:
            print("Starting Discord bot...")
            load_cogs(bot)
            bot.run(os.environ.get('DISCORD_TOKEN'))
        except Exception as e:
            print(f"Error starting Discord bot: {e}")

# Main execution
if __name__ == "__main__":
    # Create threads for Flask and Discord bot
    if flask_enabled:
        flask_thread = threading.Thread(target=run_flask)
        flask_thread.start()
        
    if discord_enabled:
        discord_thread = threading.Thread(target=run_discord_bot)
        discord_thread.start() 
        
    # Join threads to the main thread
    if flask_enabled:
        flask_thread.join()
        
    if discord_enabled:
        discord_thread.join()