import os
import pyautogui
import pytchat
import minescript
import time
import keyboard
import mouse
import random
import threading

# Set environment variable for the home directory
if os.name == 'nt':
    os.environ['USERPROFILE'] = os.getenv('USERPROFILE', 'C:\\Users\\Default')
else:
    os.environ['HOME'] = os.getenv('HOME', '/home/default')

# Dictionary to track cooldowns for each user
user_cooldowns = {}
category_cooldowns = {}  # Tracks category cooldowns globally
user_last_command = {}
user_summon_cooldowns = {}  # Stores cooldowns per user (by category)
user_last_summon = {}  # Tracks last summoned category per user
user_hostile_cooldowns = {}  # Tracks last hostile mob summon per user
cooldowns = {}
tickrate_cooldowns = {}


# Function to handle cooldowns and prevent spam
def execute_with_cooldown(user, command_name, cooldown_time, function):
    """Execute command with anti-spam and cooldown checks."""
    if user not in user_cooldowns:
        user_cooldowns[user] = {}

    # Check if the user is trying to repeat the same command twice in quick succession
    if user in user_last_command and user_last_command[user] == command_name:
        minescript.echo(f"{user}, you cannot use {command_name} twice in a row!")
        return

    # Check if the command is still on cooldown
    if command_name in user_cooldowns[user] and time.time() < user_cooldowns[user][command_name]:
        remaining_time = round(user_cooldowns[user][command_name] - time.time(), 1)
        minescript.echo(f"{user}, please wait {remaining_time} seconds before using {command_name} again.")
        return

    # Update cooldown timer for the user
    user_cooldowns[user][command_name] = time.time() + cooldown_time
    user_last_command[user] = command_name  # Track the last used command

    # Run the function in a separate thread to not block the main thread
    threading.Thread(target=function, daemon=True).start()

# Function to process chat messages dynamically
def fetch_youtube_chat(video_id):
    try:
        minescript.echo("Starting Crowd Control v2.0.0")
        chat = pytchat.create(video_id=video_id)
        while chat.is_alive():
            for c in chat.get().sync_items():
                user = c.author.name
                message = c.message.strip()  # Ensure no extra spaces

                if '!screenshot' in c.message:
                    screenshot_command(c.message, user)

                if '!perspective' in c.message:
                    perspective_command(c.message, user)

                if '!selfie' in c.message:
                    selfie_command(c.message, user)

                if '!hud' in c.message:
                    hud_command(c.message, user)

                if '!debug' in c.message:
                    debug_command(c.message, user)

                if '!attack' in c.message:
                    attack_command(c.message, user)

                if '!use' in c.message:
                    use_command(c.message, user)

                if '!pick' in c.message:
                    pick_command(c.message, user)

                if '!chat' in c.message:
                    chat_command(c.message, user)

                if '!inventory' in c.message:
                    inventory_command(c.message, user)

                if '!swap' in c.message:
                    swap_command(c.message, user)

                if '!180' in c.message:
                    flip_command(c.message, user)

                if '!seed' in c.message:
                    seed_command(c.message, user)

                if '!list' in c.message:
                    list_command(c.message, user)

                if '!particle' in c.message:
                    particle_command(c.message, user)

                if '!sound' in c.message:
                    sound_command(c.message, user)

                if '!invincible' in c.message:
                    invincible_command(c.message, user)

                if '!fling' in c.message:
                    fling_command(c.message, user)

                if '!chorus' in c.message:
                    chorus_command(c.message, user)

                if '!dig' in c.message:
                    dig_command(c.message, user)

                if '!cobweb' in c.message:
                    cobweb_command(c.message, user)

                if '!dev' in c.message:
                    dev_command(c.message, user)

                if '!move' in c.message:
                    movement_command(c.message, user)

                if '!slot' in c.message:
                    slot_command(c.message, user)

                if '!gamemode' in c.message:
                    gamemode_command(c.message, user)

                if '!timeset' in c.message:
                    timeset_command(c.message, user)

                if '!locate' in c.message:
                    locate_command(c.message, user)

                if '!tickrate' in c.message:
                    tickrate_command(c.message, user)

                if '!ride' in c.message:
                    ride_command(c.message, user)

                if '!exp' in c.message:
                    exp_command(c.message, user)

                if '!scale' in c.message:
                    scale_command(c.message, user)

                if '!give' in c.message:
                    give_command(c.message, user)

                if '!summon' in c.message:
                    summon_command(c.message, user)

                if '!weather' in c.message:
                    weather_command(c.message, user)                    

                if '!difficulty' in c.message:
                    difficulty_command(c.message, user)

                if '!gravity' in c.message:
                    gravity_command(c.message, user)

                if '!speed' in c.message:
                    speed_command(c.message, user)

                if '!damage' in c.message:
                    damage_command(c.message, user)

                if '!heal' in c.message:
                    heal_command(c.message, user)

                if '!hunger' in c.message:
                    hunger_command(c.message, user)

                if '!feed' in c.message:
                    feed_command(c.message, user)
                
                if '!nojump' in c.message:
                    nojump_command(c.message, user)

                if '!scramble' in c.message:
                    scramble_command(c.message, user)

                if '!drop' in c.message:
                    drop_command(c.message, user)

                if '!effect' in c.message:
                    effect_command(c.message, user)

                if '!enchant' in c.message:
                    enchant_command(c.message, user)

    except Exception as e:
        minescript.echo(f"An error occurred: {e}")

############################################################################################################

def screenshot_command(message, user):  # Function to process screenshot command in chat
    command_parts = message.split()     # Extract the command
    if command_parts[0].lower() == "!screenshot":       # Ensure the command is correct
        def execute_screenshot():
            pyautogui.hotkey('f2')
            minescript.echo(f"{user} took a screenshot")
        execute_with_cooldown(user, "!screenshot", 2.5, execute_screenshot)     # Apply cooldown to the command

############################################################################################################

def perspective_command(message, user): # Function to process F5 in chat
    command_parts = message.split()     # Extract the command
    if command_parts[0].lower() == "!perspective":      # Ensure the command is correct
        def execute_perspective():
            minescript.press_key_bind("key.togglePerspective", True)
            minescript.echo(f"{user} changed your perspective")
        execute_with_cooldown(user, "!perspective", 5, execute_perspective)     # Apply cooldown to the command

############################################################################################################

def selfie_command(message, user):      # Function to process F5 twice in chat
    command_parts = message.split()     # Extract the command
    if command_parts[0].lower() == "!selfie":       # Ensure the command is correct
        def execute_selfie():
            minescript.press_key_bind("key.togglePerspective", True)
            minescript.press_key_bind("key.togglePerspective", True)
            minescript.echo(f"{user} changed your perspective")
        execute_with_cooldown(user, "!selfie", 5, execute_selfie)       # Apply cooldown to the command

############################################################################################################

def hud_command(message, user):     # Function to process F1 in chat
    command_parts = message.split() # Extract the command
    if command_parts[0].lower() == "!hud":      # Ensure the command is correct
        def execute_hud():
            pyautogui.hotkey('f1')
            minescript.echo(f"{user} changed your hud")
        execute_with_cooldown(user, "!hud", 2.5, execute_hud)   # Apply cooldown to the command

############################################################################################################

def debug_command(message, user):   # Function to process F3 in chat
    command_parts = message.split() # Extract the command
    if command_parts[0].lower() == "!debug":    # Ensure the command is correct
        def execute_debug():
            pyautogui.hotkey('f3')
            minescript.echo(f"{user} opened your debug screen")
        execute_with_cooldown(user, "!debug", 2.5, execute_debug) # Apply cooldown to the command

############################################################################################################

def attack_command(message, user):  # Function to process the attack command in chat
    command_parts = message.split() # Extract the command
    if command_parts[0].lower() == "!attack":   # Ensure the command is correct
        def execute_attack():
            minescript.press_key_bind("key.attack", True)
            minescript.press_key_bind("key.attack", False)
            minescript.echo(f"{user} made you attack")
        execute_with_cooldown(user, "!attack", 2.5, execute_attack)   # Apply cooldown to the command

############################################################################################################

def use_command(message, user):     # Function to process the use command in chat
    command_parts = message.split() # Extract the command
    if command_parts[0].lower() == "!use":  # Ensure the command is correct
        def execute_use():
            minescript.press_key_bind("key.use", True)
            minescript.press_key_bind("key.use", False)
            minescript.echo(f"{user} used your item")
        execute_with_cooldown(user, "!use", 2.5, execute_use) # Apply cooldown to the command

############################################################################################################

def pick_command(message, user):    # Function to process the pick command in chat
    command_parts = message.split() # Extract the command
    if command_parts[0].lower() == "!pick": # Ensure the command is correct
        def execute_pick():
            minescript.press_key_bind("key.pickItem", True)
            minescript.press_key_bind("key.pickItem", False)
            minescript.echo(f"{user} picked your block")
        execute_with_cooldown(user, "!pick", 2.5, execute_pick) # Apply cooldown to the command

############################################################################################################

def chat_command(message, user):    # Function to process the chat command in chat
    command_parts = message.split() # Extract the command
    if command_parts[0].lower() == "!chat": # Ensure the command is correct
        def execute_chat():
            minescript.press_key_bind("key.chat", True)
            minescript.press_key_bind("key.chat", False)
            minescript.echo(f"{user} opened chat")
        execute_with_cooldown(user, "!chat", 5, execute_chat)   # Apply cooldown to the command

############################################################################################################

def inventory_command(message, user):   # Function to process the inventory command in chat
    command_parts = message.split()     # Extract the command
    if command_parts[0].lower() == "!inventory":    # Ensure the command is correct
        def execute_inventory():
            minescript.press_key_bind("key.inventory", True)
            minescript.press_key_bind("key.inventory", False)
            minescript.echo(f"{user} opened your inventory")
        execute_with_cooldown(user, "!inventory", 5, execute_inventory) # Apply cooldown to the command

############################################################################################################

def swap_command(message, user):    # Function to process the swap command in chat
    command_parts = message.split() # Extract the command
    if command_parts[0].lower() == "!swap": # Ensure the command is correct
        def execute_swap():
            minescript.press_key_bind("key.swapOffhand", True)
            minescript.press_key_bind("key.swapOffhand", False)
            minescript.echo(f"{user} swapped your items")
        execute_with_cooldown(user, "!swap", 5, execute_swap)   # Apply cooldown to the command

############################################################################################################

def flip_command(message, user):    # Function to process the 180 command in chat
    command_parts = message.split() # Extract the command
    if command_parts[0].lower() == "!180":  # Ensure the command is correct
        def execute_flip():
            minescript.execute("/tp @a ~ ~ ~ ~180 ~")
            minescript.echo(f"{user} turned you around")
        execute_with_cooldown(user, "!180", 10, execute_flip)    # Apply cooldown to the command

############################################################################################################

def seed_command(message, user):    # Function to process the seed command in chat
    command_parts = message.split() # Extract the command
    if command_parts[0].lower() == "!seed": # Ensure the command is correct
        def execute_seed():
            minescript.echo(f"{user} checked your seed")
            minescript.execute("/seed")
        execute_with_cooldown(user, "!seed", 2.5, execute_seed) # Apply cooldown to the command

############################################################################################################

def list_command(message, user):    # Function to process the list command in chat
    command_parts = message.split() # Extract the command
    if command_parts[0].lower() == "!list": # Ensure the command is correct
        def execute_list():
            minescript.execute("/list")
            minescript.echo(f"{user} wanted to see who was online")
        execute_with_cooldown(user, "!list", 2.5, execute_list)   # Apply cooldown to the command

############################################################################################################

def particle_command(message, user):  # Function to process particle command in chat
    command_parts = message.split()  # Extract the command
    if command_parts[0].lower() == "!particle":  # Ensure the command is correct
        if len(command_parts) < 2:  # Ensure a particle type is specified
            minescript.echo(f"{user}, please specify a particle type. Usage: !particle <particle_name>")
            return
        particle_type = command_parts[1].lower()  # Extract the particle type
        def execute_particle():
            try:
                minescript.execute(f"/particle minecraft:{particle_type} ~ ~1 ~ 1 1 1 0.01 250 force")  # Execute the particle command
                minescript.echo(f"{user} created a {particle_type} particle effect!")  # Send the particle message
            except Exception as e:
                minescript.echo(f"Failed to create particle '{particle_type}'. Please ensure it's a valid particle. Error: {str(e)}")
        execute_with_cooldown(user, "!particle", 2.5, execute_particle)  # 2.5 seconds cooldown for particle command

############################################################################################################

def sound_command(message, user):  # Function to process the sound command in chat
    command_parts = message.split()  # Extract the command
    if command_parts[0].lower() == "!sound":  # Ensure the command is correct
        if len(command_parts) < 2:  # Ensure a sound type is specified
            minescript.echo(f"{user}, please specify a sound. Usage: !sound <sound_name>")
            return
        sound_type = command_parts[1].lower()  # Extract the sound type
        def execute_sound():
            try:
                minescript.execute(f"/playsound minecraft:{sound_type} master @a ~ ~ ~ 1 1 1")  # Execute the playsound command
                minescript.echo(f"{user} played the sound {sound_type}!")  # Send the sound message
            except Exception as e:
                minescript.echo(f"Failed to play sound '{sound_type}'. Please ensure it's a valid sound. Error: {str(e)}")
        execute_with_cooldown(user, "!sound", 2.5, execute_sound)  # 2.5 seconds cooldown for sound command

############################################################################################################

def invincible_command(message, user):  # Function to process the invincible command in chat
    command_parts = message.split()     # Extract the command
    if command_parts[0].lower() == "!invincible":   # Ensure the command is correct
        def execute_invincible():
            minescript.execute("/effect give @p resistance 10 5 true", )
            minescript.execute("/effect give @p absorption 10 255 true")
            minescript.execute("/effect give @p fire_resistance 10 1 true")
            minescript.execute("/effect give @p regeneration 10 255 true")
            minescript.echo(f"{user} made you invincible for 10 seconds")
        execute_with_cooldown(user, "!invincible", 30, execute_invincible)   # Apply cooldown to the command

############################################################################################################

def fling_command(message, user):   # Function to process the fling command in chat
    command_parts = message.split() # Extract the command
    if command_parts[0].lower() == "!fling":    # Ensure the command is correct
        def execute_fling():
            minescript.execute("/effect give @p minecraft:levitation 1 255")
            time.sleep(0.5)
            minescript.execute("/effect clear @p")
            time.sleep(2)
            minescript.echo(f"{user} flung you into the air")
            time.sleep(2)
            minescript.execute("/attribute @p minecraft:generic.fall_damage_multiplier base set 0")
            time.sleep(7)
            minescript.execute("/attribute @p minecraft:generic.fall_damage_multiplier base set 1")
        execute_with_cooldown(user, "!fling", 30, execute_fling) # Apply cooldown to the command

############################################################################################################

def chorus_command(message, user):  # Function to process the chorus fruit commands in chat
    command_parts = message.split() # Extract the command
    if command_parts[0].lower() == "!chorus":   # Ensure the command is correct
        def execute_chorus():
            minescript.execute("/playsound minecraft:item.chorus_fruit.teleport player @p")
            minescript.execute("/spreadplayers ~ ~ 0 8 false @p")
            minescript.echo(f"{user} made you eat a chorus fruit")
        execute_with_cooldown(user, "!chorus", 30, execute_chorus)  # Apply cooldown to the command

############################################################################################################

def dig_command(message, user):     # Function to process the dig command in chat
    command_parts = message.split() # Extract the command
    if command_parts[0].lower() == "!dig":  # Ensure the command is correct
        def execute_dig():
            minescript.execute("/execute as @p at @p run setblock ~ ~-1 ~ air destroy")
            minescript.echo(f"{user} dug a block under you")
        execute_with_cooldown(user, "!dig", 30, execute_dig)    # Apply cooldown to the command

############################################################################################################

def cobweb_command(message, user):      # Function to process the cobweb command in chat
    command_parts = message.split()     # Extract the command
    if command_parts[0].lower() == "!cobweb":   # Ensure the command is correct
        def execute_cobweb():
            minescript.execute("/execute as @p at @p run setblock ~ ~ ~ minecraft:cobweb")
            minescript.echo(f"{user} placed a cobweb on you")
        execute_with_cooldown(user, "!cobweb", 15, execute_cobweb)  # Apply cooldown to the command

############################################################################################################

dev_commands = {    # Define the dev commands and their corresponding actions
    "notch": "/give @p minecraft:enchanted_golden_apple",  # Notch apple command
    "dinnerbone": "/give @p minecraft:name_tag[custom_name=Dinnerbone]",  # Dinnerbone nametag
    "grumm": "/give @p minecraft:name_tag[custom_name=Grumm]",  # Grumm nametag
    "_jeb": "/give @p minecraft:name_tag[custom_name=_jeb]",  # _jeb nametag
}
def dev_command(message, user): # Function to process dev commands in chat
    command_parts = message.split() # Extract the dev command after the command
    if len(command_parts) > 1:  # Ensure there is something after '!dev'
        dev_command_name = command_parts[1].lower()
        if dev_command_name in dev_commands:    # Check if the dev command is valid
            def execute_dev_command():  # Define the function to execute the dev command
                minescript.execute(dev_commands[dev_command_name])  # Execute the dev command (e.g., give items or summon)
                if dev_command_name == "notch": # Customize the message based on the dev command
                    minescript.echo(f"{user} gave you a Notch apple!")
                elif dev_command_name == "dinnerbone":
                    minescript.echo(f"{user} gave you a Dinnerbone nametag!")
                elif dev_command_name == "grumm":
                    minescript.echo(f"{user} gave you a Grumm nametag!")
                elif dev_command_name == "jeb":
                    minescript.echo(f"{user} gave you a _jeb nametag!")
                else:
                    minescript.echo(f"{user} used the {dev_command_name} dev command!")
            execute_with_cooldown(user, f"!dev {dev_command_name}", 5, execute_dev_command) # Apply the appropriate cooldown based on the command
        else:
            valid_dev_commands = ", ".join(dev_commands.keys()) # Provide personalized guidance if an invalid dev command is used
            minescript.echo(f"Hey {user}, that’s not a valid dev command! Try using one of these: {valid_dev_commands}")

############################################################################################################

movement_conditions = { # Define movement commands and their corresponding key bindings
    "forward": "key.forward", "back": "key.back", "left": "key.left",
    "right": "key.right", "jump": "key.jump", "sneak": "key.sneak"
}
def movement_command(message, user):    # Function to process movement commands in chat
    command_parts = message.split() # Extract the movement condition after the command
    if len(command_parts) > 1:  # Ensure there is something after '!move'
        movement_condition = command_parts[1].lower()
        if movement_condition in movement_conditions:   # Check if the condition is valid (forward, back, left, right, jump, sneak)
            def execute_movement(): # Define the function to execute the movement
                minescript.press_key_bind(movement_conditions[movement_condition], True)
                time.sleep(0.5)
                minescript.press_key_bind(movement_conditions[movement_condition], False)
                action_message = (  # Adjust the message for "jump" and "sneak" for better grammar
                    f"{user} made you {movement_condition}"
                    if movement_condition in ["jump", "sneak"]
                    else f"{user} made you move {movement_condition}"
                )
                minescript.echo(action_message)
            execute_with_cooldown(user, f"!move {movement_condition}", 2.5, execute_movement)   # Apply cooldown to the movement command
        else:
            valid_moves = ", ".join(movement_conditions.keys()) # Provide guidance if an invalid movement condition is used
            minescript.echo(f"{user}, that’s not a valid move! Try using one of these: {valid_moves}")

############################################################################################################

hotbar_conditions = {   # Define slot commands and their corresponding key bindings
    "1": "key.hotbar.1", "2": "key.hotbar.2", "3": "key.hotbar.3",
    "4": "key.hotbar.4", "5": "key.hotbar.5", "6": "key.hotbar.6",
    "7": "key.hotbar.7", "8": "key.hotbar.8", "9": "key.hotbar.9"
}
def slot_command(message, user):    # Function to process slot switch commands in chat
    command_parts = message.split()     # Extract the slot number after the command
    if len(command_parts) > 1:  # Ensure there is something after '!slot'
        hotbar_slot = command_parts[1]
        if hotbar_slot in hotbar_conditions:    # Check if the slot is valid (1 through 9)
            def execute_slot_switch():  # Define the function to execute the slot switch
                minescript.press_key_bind(hotbar_conditions[hotbar_slot], True)
                minescript.echo(f"{user} switched to slot {hotbar_slot}")
            execute_with_cooldown(user, f"!slot {hotbar_slot}", 2.5, execute_slot_switch)   # Apply cooldown to the slot command
        else:
            valid_slots = ", ".join(hotbar_conditions.keys())   # Provide personalized guidance if an invalid slot number is used
            minescript.echo(f"{user}, that’s not a valid slot! You can use one of these: {valid_slots}")

############################################################################################################

def gamemode_command(message, user):    # Define the gamemode command and associated actions
    global cooldowns
    command_parts = message.split()
    if len(command_parts) > 1:
        gamemode = command_parts[1].lower()
        gamemode_durations = {
            "creative": 20, "spectator": 10, "adventure": 20,
        }
        cooldown_time = 60  # Cooldown duration in seconds
        if user in cooldowns and time.time() - cooldowns[user] < cooldown_time: # Check if the user is on cooldown
            remaining_time = round(cooldown_time - (time.time() - cooldowns[user]), 1)
            minescript.echo(f"{user}, you must wait {remaining_time} more seconds before using !gamemode again.")
            return
        if gamemode in gamemode_durations:
            cooldowns[user] = time.time()  # Set cooldown timestamp
            def execute_gamemode():
                if gamemode == "creative":
                    minescript.execute("/gamemode creative")
                    keyboard.block_key("e")  # Disable 'E' key
                    minescript.echo(f"{user} switched you to Creative mode for {gamemode_durations['creative']} seconds!")
                    time.sleep(gamemode_durations["creative"])
                    minescript.execute("/gamemode survival")
                    keyboard.unblock_key("e")  # Restore 'E' key
                    minescript.echo("Returning to Survival mode. 'E' key is now enabled.")
                elif gamemode == "spectator":
                    minescript.execute("/gamemode spectator")
                    minescript.echo(f"{user} switched you to Spectator mode for {gamemode_durations['spectator']} seconds!")
                    time.sleep(gamemode_durations["spectator"])
                    minescript.execute("/gamemode survival")
                    minescript.echo("Returning to Survival mode")
                elif gamemode == "adventure":
                    minescript.execute("/gamemode adventure")
                    minescript.echo(f"{user} switched you to Adventure mode for {gamemode_durations['adventure']} seconds!")
                    time.sleep(gamemode_durations["adventure"])
                    minescript.execute("/gamemode survival")
                    minescript.echo("Returning to Survival mode")
            threading.Thread(target=execute_gamemode, daemon=True).start()  # Run in a separate thread to avoid blocking other commands
        else:
            valid_modes = ", ".join(gamemode_durations.keys())
            minescript.echo(f"Invalid gamemode! Use one of these: {valid_modes}")

############################################################################################################

time_options = {    # Define valid time options
    "day": 1000,        
    "noon": 6000,       
    "night": 13000,     
    "midnight": 18000   
}
def timeset_command(message, user):
    command_parts = message.split()
    if len(command_parts) < 2:
        minescript.echo(f"{user}, please use the correct format: !timeset <time_option/custom_value>")
        return
    time_input = command_parts[1].lower()
    def execute_timeset():  # Define the function to execute after cooldown check
        if time_input in time_options:
            time_value = time_options[time_input]
            minescript.execute(f"/time set {time_value}")
            minescript.echo(f"{user} set the time to {time_input} ({time_value})")
        elif time_input.isdigit():
            custom_value = int(time_input)
            if 0 <= custom_value <= 24000:
                minescript.execute(f"/time set {custom_value}")
                minescript.echo(f"{user} set the time to {custom_value}")
            else:
                minescript.echo(f"{user}, invalid custom time! Please enter a value between 0 and 24000.")
        else:
            minescript.echo(f"{user}, invalid time option! Valid options: day, noon, night, midnight, or a custom value between 0 and 24000.")
    execute_with_cooldown(user, "!timeset", 600, execute_timeset)   # Use the cooldown function to manage cooldowns

############################################################################################################

locate_options = {  # Define valid biomes and structures
    "biome": ["plains", "sunflower_plains", "meadow", "forest", "birch_forest", "old_growth_birch_forest", "dark_forest",
        "flower_forest", "old_growth_pine_taiga", "old_growth_spruce_taiga", "windswept_forest", "jungle", "sparse_jungle",
        "bamboo_jungle", "savanna", "savanna_plateau", "windswept_savanna", "desert", "eroded_badlands", "badlands", "wooded_badlands",
        "jagged_peaks", "frozen_peaks", "stony_peaks", "taiga", "snowy_taiga", "snowy_plains", "snowy_slopes", "ice_spikes",
        "frozen_river", "swamp", "mangrove_swamp", "beach", "snowy_beach", "stony_shore", "lush_caves", "dripstone_caves",
        "deep_dark", "warm_ocean", "lukewarm_ocean", "deep_lukewarm_ocean", "cold_ocean", "deep_cold_ocean", "frozen_ocean",
        "deep_frozen_ocean", "ocean", "deep_ocean", "nether_wastes", "crimson_forest", "warped_forest", "soul_sand_valley",
        "basalt_deltas", "the_end", "small_end_islands", "end_midlands", "end_highlands", "end_barrens", "river", "the_void",
        "pale_garden"],
    "structure": ["ancient_city", "stronghold", "village_desert", "village_plains", "village_savanna", "village_snowy",
        "village_taiga", "desert_pyramid", "jungle_pyramid", "swamp_hut", "igloo", "woodland_mansion", "mineshaft",
        "trail_ruins", "trial_chambers", "buried_treasure", "ocean_monument", "ocean_ruins", "shipwreck", "pillager_outpost",
        "ruined_portal", "fortress", "bastion_remnant", "ruined_portal_nether", "nether_fossil", "end_city", "the_end"],
}
def locate_command(message, user):
    command_parts = message.split()
    if len(command_parts) < 3:
        minescript.echo(f"{user}, please use the correct format: !locate <biome/structure> <name>")
        return
    category = command_parts[1].lower()
    target = command_parts[2].lower()
    if category not in locate_options:  # Check if the category is valid
        minescript.echo(f"{user}, invalid category! Use 'biome' or 'structure'.")
        return
    if target not in locate_options[category]:  # Check if the target exists in the selected category
        valid_list = ", ".join(locate_options[category])
        minescript.echo(f"{user}, invalid {category}! Valid options: {valid_list}")
        return
    def execute_locate():   # Execute the locate command asynchronously
        minescript.execute(f"/locate {category} {target}")
        minescript.echo(f"{user} requested location for {category}: {target}")
    execute_with_cooldown(user, f"!locate {category}", 7.5, execute_locate)  # Apply cooldown

############################################################################################################

tickrate_options = {  # Define valid tick rate categories
    "freeze": "freeze",  # Represents freezing the tick rate
}
def tickrate_command(message, user):
    command_parts = message.split()
    if len(command_parts) < 2:
        minescript.echo(f"{user}, please use the correct format: !tickrate <freeze/integer>")
        return
    tickrate_input = command_parts[1].lower()
    def execute_tickrate():  # Define the function to execute after cooldown check
        if tickrate_input == "freeze":
            try:
                minescript.execute("/tick freeze")  # Execute the freeze command
                minescript.echo(f"{user} froze the tick rate for 30 seconds!")
                time.sleep(30)  # Wait 30 seconds before resetting
                minescript.execute("/tick unfreeze")
                minescript.echo("Tick rate unfrozen.")
                time.sleep(15)
            except Exception as e:
                minescript.echo(f"Failed to freeze tick rate. Error: {str(e)}")
        elif tickrate_input.isdigit():
            try:
                tick_rate = int(tickrate_input)
                if 2 <= tick_rate <= 200:   # Ensure tick rate is within allowed limits
                    try:
                        minescript.execute(f"/tick rate {tick_rate}")   # Execute the command to change tick speed
                        minescript.echo(f"{user} set the tick rate to {tick_rate} for 30 seconds!")
                        time.sleep(30)  # Wait 30 seconds before resetting
                        minescript.execute("/tick rate 20")
                        minescript.echo("The tick rate has reset.")
                        time.sleep(15)
                    except Exception as e:
                        minescript.echo(f"Failed to change tick rate. Error: {str(e)}")
                else:
                    minescript.echo(f"{user}, please specify a tick rate between 2 and 200.")
            except ValueError:
                minescript.echo(f"{user}, invalid tick rate. Please enter a number between 2 and 200.")
        else:
            minescript.echo(f"{user}, invalid tick rate option! Valid options: 'freeze' or an integer between 2 and 200.")
    execute_with_cooldown(user, "!tickrate", 150, execute_tickrate) # Use execute_with_cooldown to check cooldown and execute the command

############################################################################################################

def get_mob_category(mob):
    mob_categories = {
        # Passive Mobs
        "allay": "passive", "armadillo": "passive", "axolotl": "passive", "bat": "passive", 
        "camel": "passive", "cat": "passive", "chicken": "passive", "cod": "passive", 
        "cow": "passive", "donkey": "passive", "frog": "passive", "glow_squid": "passive", 
        "horse": "passive", "mooshroom": "passive", "mule": "passive", "ocelot": "passive", 
        "parrot": "passive", "pig": "passive", "pufferfish": "passive", "rabbit": "passive", 
        "salmon": "passive", "sheep": "passive", "skeleton_horse": "passive", "sniffer": "passive", 
        "snow_golem": "passive", "squid": "passive", "strider": "passive", "tadpole": "passive", 
        "tropical_fish": "passive", "turtle": "passive", "villager": "passive", "wandering_trader": "passive",

        # Neutral Mobs
        "bee": "neutral", "cave_spider": "neutral", "dolphin": "neutral", "drowned": "neutral", 
        "enderman": "neutral", "fox": "neutral", "goat": "neutral", "iron_golem": "neutral", 
        "llama": "neutral", "panda": "neutral", "piglin": "neutral", "polar_bear": "neutral", 
        "spider": "neutral", "trader_llama": "neutral", "wolf": "neutral", "zombified_piglin": "neutral",

        # Hostile Mobs
        "blaze": "hostile", "breeze": "hostile", "creaking": "hostile", "endermite": "hostile", 
        "evoker": "hostile", "guardian": "hostile", "hoglin": "hostile", "husk": "hostile", 
        "magma_cube": "hostile", "phantom": "hostile", "zoglin": "hostile", "pillager": "hostile", 
        "shulker": "hostile", "silverfish": "hostile", "skeleton": "hostile", "slime": "hostile", 
        "stray": "hostile", "vex": "hostile", "zombie": "hostile", "zombie_villager": "hostile",

        # Super Hostile Mobs
        "bogged": "super_hostile", "ravager": "super_hostile", "wither_skeleton": "super_hostile", 
        "piglin_brute": "super_hostile", "vindicator": "super_hostile", "elder_guardian": "super_hostile", 
        "warden": "super_hostile", "ghast": "super_hostile", "creeper": "super_hostile"
    }
    
    # Return the mob category or 'unknown' if the mob is not found
    return mob_categories.get(mob, "unknown")
mob_category_cooldowns = {  # Define cooldown time for each mob category in seconds
    "passive": 2.5,  # 1 minute cooldown for passive mobs
    "neutral": 5,  # 1.5 minute cooldown for neutral mobs
    "hostile": 20,  # 2 minute cooldown for hostile mobs
    "super_hostile": 120,  # 3 minute cooldown for super hostile mobs
}
def ride_command(message, user):
    command_parts = message.split()
    if len(command_parts) > 1:
        mob = command_parts[1].lower()
        mob_category = get_mob_category(mob)  # Get the mob's category
        cooldown_time = mob_category_cooldowns.get(mob_category, 60)  # Default to 60 seconds if category is unknown
        def execute_ride():
            try:
                minescript.execute(f"/ride @p mount @n[type=minecraft:{mob},distance=..16]")    # Summon the mob and mount the player to it (as long as it's not restricted)
                minescript.echo(f"{user} is now riding a {mob}!")
            except Exception as e:
                minescript.echo(f"Failed to ride '{mob}'. Error: {str(e)}")
        execute_with_cooldown(user, "!ride", cooldown_time + 15, execute_ride)  # Call execute_with_cooldown to check cooldown and execute the logic
    else:
        minescript.echo(f"{user}, please specify a mob to ride. Usage: !ride <mob>")

############################################################################################################

def exp_command(message, user):
    """Handles the experience command with cooldowns and validation."""
    global user_last_command
    command_parts = message.split()
    if len(command_parts) < 2:
        minescript.echo(f"{user}, please use the correct format: !exp <give/take/reset> <experience_number>")
        return
    action = command_parts[1].lower()  # Extract "give", "take", or "reset"
    cooldowns = {   # Define cooldown times (in seconds)
        "give": 10,
        "take": 30,
        "reset": 120
    }
    if action not in cooldowns:
        minescript.echo(f"{user}, invalid action. Valid options: 'give', 'take', or 'reset'.")
        return
    if user in user_last_command and user_last_command[user] == "!exp": # Global Anti-Spam Check (Prevents immediate re-use of !exp in any form)
        minescript.echo(f"{user}, you cannot use {user_last_command[user]} twice in a row!")
        return
    def execute_exp():
        global user_last_command
        if action == "reset":
            minescript.execute("/xp add @p -2100000000 levels")  # Reset experience
            minescript.echo(f"{user} reset the player's experience!")
        else:
            if len(command_parts) < 3:
                minescript.echo(f"{user}, please specify a valid experience number. Usage: !exp <give/take/reset> <experience_number>")
                return
            try:
                exp_value = int(command_parts[2])
            except ValueError:
                minescript.echo(f"{user}, please specify a valid experience number. Usage: !exp <give/take/reset> <experience_number>")
                return
            if action == "give":
                minescript.execute(f"/xp add @p {exp_value} levels")
                minescript.echo(f"{user} gave {exp_value} experience levels!")
            elif action == "take":
                minescript.execute(f"/xp add @p {-exp_value} levels")  # Negative XP to remove levels
                minescript.echo(f"{user} took {exp_value} experience levels!")
        user_last_command[user] = "!exp"    # Mark `!exp` as the last successful command
    cooldown_key = f"!exp_{action}"  # Unique key for each subcommand
    execute_with_cooldown(user, cooldown_key, cooldowns[action], execute_exp)

############################################################################################################

def get_mob_category(mob):
    mob_categories = {
        # Player
        "player": "player",
        
        # Passive Mobs
        "allay": "passive", "armadillo": "passive", "axolotl": "passive", "bat": "passive", 
        "camel": "passive", "cat": "passive", "chicken": "passive", "cod": "passive", 
        "cow": "passive", "donkey": "passive", "frog": "passive", "glow_squid": "passive", 
        "horse": "passive", "mooshroom": "passive", "mule": "passive", "ocelot": "passive", 
        "parrot": "passive", "pig": "passive", "pufferfish": "passive", "rabbit": "passive", 
        "salmon": "passive", "sheep": "passive", "skeleton_horse": "passive", "sniffer": "passive", 
        "snow_golem": "passive", "squid": "passive", "strider": "passive", "tadpole": "passive", 
        "tropical_fish": "passive", "turtle": "passive", "villager": "passive", "wandering_trader": "passive",

        # Neutral Mobs
        "bee": "neutral", "cave_spider": "neutral", "dolphin": "neutral", "drowned": "neutral", 
        "enderman": "neutral", "fox": "neutral", "goat": "neutral", "iron_golem": "neutral", 
        "llama": "neutral", "panda": "neutral", "piglin": "neutral", "polar_bear": "neutral", 
        "spider": "neutral", "trader_llama": "neutral", "wolf": "neutral", "zombified_piglin": "neutral",

        # Hostile Mobs
        "blaze": "hostile", "breeze": "hostile", "creaking": "hostile", "endermite": "hostile", 
        "evoker": "hostile", "guardian": "hostile", "hoglin": "hostile", "husk": "hostile", 
        "magma_cube": "hostile", "phantom": "hostile", "zoglin": "hostile", "pillager": "hostile", 
        "shulker": "hostile", "silverfish": "hostile", "skeleton": "hostile", "slime": "hostile", 
        "stray": "hostile", "vex": "hostile", "zombie": "hostile", "zombie_villager": "hostile",

        # Super Hostile Mobs
        "bogged": "super_hostile", "ravager": "super_hostile", "wither_skeleton": "super_hostile", 
        "piglin_brute": "super_hostile", "vindicator": "super_hostile", "elder_guardian": "super_hostile", 
        "warden": "super_hostile", "ghast": "super_hostile", "creeper": "super_hostile"
    }
    
    # Return the mob category or 'unknown' if the mob is not found
    return mob_categories.get(mob, "unknown")
mob_category_cooldowns = {  # Define cooldown time for each mob category in seconds
    "player": 60,
    "passive": 120,  # 1 minute cooldown for passive mobs
    "neutral": 240,  # 1.5 minute cooldown for neutral mobs
    "hostile": 480,  # 2 minute cooldown for hostile mobs
    "super_hostile": 600,  # 3 minute cooldown for super hostile mobs
}
def scale_command(message, user):
    global user_last_command
    command_parts = message.split()
    if len(command_parts) < 3:
        minescript.echo(f"{user}, please specify an entity and a scale value. Usage: !scale <entity> <value>")
        return
    entity_type = command_parts[1].lower()  # Extract entity type
    try:
        scale_value = float(command_parts[2])  # Extract scale value
    except ValueError:
        minescript.echo(f"{user}, invalid scale value. Please enter a number between 0.05 and 20.")
        return
    if scale_value > 20:    # Apply the defaulting logic
        scale_value = 20
    elif scale_value < 0.05:
        scale_value = 0.05
    if user in user_last_command and user_last_command[user] == "!scale":   # Global Anti-Spam Check (Prevents immediate re-use of !scale in any form)
        minescript.echo(f"{user}, you must use a different command before using !scale again!")
        return
    if entity_type == "player": # Check if entity is a player
        mob_category = "player"
    else:
        mob_category = get_mob_category(entity_type)    # Get the mob category using the mob dictionary for mobs that are not players
    if mob_category == "unknown":
        cooldown_time = 30  # Default cooldown for unknown entities
        minescript.echo(f"{user}, the entity '{entity_type}' is unknown. Default cooldown of 30 seconds applied.")
    else:
        cooldown_time = mob_category_cooldowns.get(mob_category, 30)
    def execute_scale():
        """Executes the scale logic after cooldown check."""
        global user_last_command
        try:
            minescript.execute(f"/attribute @n[type=minecraft:{entity_type},distance=..32,limit=1] minecraft:generic.scale base set {scale_value}")
            minescript.echo(f"{user} set the scale of the nearest {entity_type} to {scale_value}!")
            if entity_type == "player":
                time.sleep(30)  # Wait 30 seconds before resetting the scale (change as needed)
                minescript.execute(f"/attribute @p minecraft:generic.scale base set 1")
                minescript.echo(f"Your scale has been reset to 1.")
        except Exception as e:
            minescript.echo(f"Failed to change scale of '{entity_type}'. Error: {str(e)}")
        user_last_command[user] = "!scale"
    execute_with_cooldown(user, "!scale", cooldown_time, execute_scale)

############################################################################################################

rarity_items = {    # --- Item Dictionaries ---
    "uncommon": {
        "sniffer_egg": "minecraft:sniffer_egg", "recovery_compass": "minecraft:recovery_compass", 
        "disc_fragment_5": "minecraft:disc_fragment_5", "nautilus_shell": "minecraft:nautilus_shell",
        "echo_shard": "minecraft:echo_shard", "pottery_sherd": "minecraft:pottery_sherd", 
        "ominous_bottle": "minecraft:ominous_bottle", "ominous_banner": "minecraft:ominous_banner", 
        "netherite_upgrade": "minecraft:netherite_upgrade", "sentry_armor_trim": "minecraft:sentry_armor_trim",
        "dune_armor_trim": "minecraft:dune_armor_trim", "coast_armor_trim": "minecraft:coast_armor_trim"
    },
    "uncommon_single_stack": {
        "creeper_charge_banner_pattern": "minecraft:creeper_charge_banner_pattern", 
        "snout_banner_pattern": "minecraft:snout_banner_pattern", "enchanted_book": "minecraft:enchanted_book"
    },
    "rare": {
        "enchanted_golden_apple": "minecraft:enchanted_golden_apple", "beacon": "minecraft:beacon",
        "nether_star": "minecraft:nether_star", "ward_armor_trim": "minecraft:ward_armor_trim"
    },
    "rare_single_stack": {
        "flow_banner_pattern": "minecraft:flow_banner_pattern", "guster_banner_pattern": "minecraft:guster_banner_pattern", 
        "trident": "minecraft:trident"
    },
    "epic": {
        "dragon_head": "minecraft:dragon_head", "dragon_egg": "minecraft:dragon_egg"
    },
    "epic_single_stack": {
        "elytra": "minecraft:elytra", "mace": "minecraft:mace"
    },
    "admin": {
        "barrier": "minecraft:barrier", "chain_command_block": "minecraft:chain_command_block",
        "impulse_command_block": "minecraft:impulse_command_block", "debug_stick": "minecraft:debug_stick",
        "command_block": "minecraft:command_block", "light": "minecraft:light", 
        "structure_block": "minecraft:structure_block", "jigsaw_block": "minecraft:jigsaw_block",
        "structure_void": "minecraft:structure_void"
    }
}
armor_tools_weapons = {
    "leather": {
        "leather_helmet": "minecraft:leather_helmet", "leather_chestplate": "minecraft:leather_chestplate",
        "leather_leggings": "minecraft:leather_leggings", "leather_boots": "minecraft:leather_boots"
    },
    "iron": {
        "iron_helmet": "minecraft:iron_helmet", "iron_chestplate": "minecraft:iron_chestplate",
        "iron_leggings": "minecraft:iron_leggings", "iron_boots": "minecraft:iron_boots",
        "iron_sword": "minecraft:iron_sword", "iron_pickaxe": "minecraft:iron_pickaxe",
        "iron_axe": "minecraft:iron_axe", "iron_shovel": "minecraft:iron_shovel",
        "iron_hoe": "minecraft:iron_hoe"
    },
    "gold": {
        "golden_helmet": "minecraft:golden_helmet", "golden_chestplate": "minecraft:golden_chestplate",
        "golden_leggings": "minecraft:golden_leggings", "golden_boots": "minecraft:golden_boots",
        "golden_sword": "minecraft:golden_sword", "golden_pickaxe": "minecraft:golden_pickaxe",
        "golden_axe": "minecraft:golden_axe", "golden_shovel": "minecraft:golden_shovel",
        "golden_hoe": "minecraft:golden_hoe"
    },
    "diamond": {
        "diamond_helmet": "minecraft:diamond_helmet", "diamond_chestplate": "minecraft:diamond_chestplate",
        "diamond_leggings": "minecraft:diamond_leggings", "diamond_boots": "minecraft:diamond_boots",
        "diamond_sword": "minecraft:diamond_sword", "diamond_pickaxe": "minecraft:diamond_pickaxe",
        "diamond_axe": "minecraft:diamond_axe", "diamond_shovel": "minecraft:diamond_shovel",
        "diamond_hoe": "minecraft:diamond_hoe"
    },
    "netherite": {
        "netherite_helmet": "minecraft:netherite_helmet", "netherite_chestplate": "minecraft:netherite_chestplate",
        "netherite_leggings": "minecraft:netherite_leggings", "netherite_boots": "minecraft:netherite_boots",
        "netherite_sword": "minecraft:netherite_sword", "netherite_pickaxe": "minecraft:netherite_pickaxe",
        "netherite_axe": "minecraft:netherite_axe", "netherite_shovel": "minecraft:netherite_shovel",
        "netherite_hoe": "minecraft:netherite_hoe"
    }
}
common_single_stack = {
    "boat": ["boat", "raft"], "chest_boat": ["chest_boat", "chest_raft"], "bed": ["bed"],
    "bundle": ["bundle"], "shulker_box": ["shulker_box"], "minecart": ["minecart"],
    "stew": ["stew", "soup"], "book": ["book"], "potion": ["potion"],
    "bucket": ["bucket"], "rod": ["fishing_rod"], "_on_a_stick": ["carrot_on_a_stick", "warped_fungus_on_a_stick"],
    "bow": ["bow"], "crossbow": ["crossbow"], "shield": ["shield"], "turtle_helmet": ["turtle_helmet"]
}
item_cooldown_times = { # --- Cooldown Time Configuration ---
    "common": 2.5, "uncommon": 5, "uncommon_single_stack": 10, "rare": 15,
    "rare_single_stack": 30, "epic": 20, "epic_single_stack": 40, "admin": 120,
    "leather": 2.5, "iron": 5, "gold": 7.5, "diamond": 12.5, "netherite": 17.5,
    "common_single_stack": 5
}
def get_item_category(item):    # --- Helper Functions ---
    for rarity, items in rarity_items.items():
        if item in items:
            return rarity
    for category, items in armor_tools_weapons.items():
        if item in items:
            return category
    for category, keywords in common_single_stack.items():
        if any(item.endswith(k) for k in keywords):
            return "common_single_stack"
    return "common"  # Default if no category found
def apply_item_cooldown(user, item):
    category = get_item_category(item)
    if category not in item_cooldown_times: # Ensure category exists in cooldown_times
        minescript.echo(f"Error: Category '{category}' not found in cooldown_times.")
        return False
    cooldown_time = item_cooldown_times[category]  # Safe to access now
    remove_expired_item_cooldowns()
    if user_last_command.get(user) == item: # --- Prevent users from spamming the same item before applying a cooldown ---
        minescript.echo(f"{user}, you cannot request {item} twice in a row!")
        return False  # Stop execution BEFORE cooldown is applied
    if user in user_cooldowns and category in user_cooldowns[user]: # --- Prevent users from requesting different items in the same category while on cooldown ---
        remaining_time = round(user_cooldowns[user][category] - time.time(), 1)
        if remaining_time > 0:
            minescript.echo(f"{user}, you must wait {remaining_time} seconds before requesting another {category} item!")
            return False  # Stop execution BEFORE cooldown is applied
    if category in category_cooldowns:  # --- Prevent global category spam ---
        remaining_time = round(category_cooldowns[category] - time.time(), 1)
        if remaining_time > 0:
            minescript.echo(f"{user}, the {category} category is on cooldown for {remaining_time} more seconds!")
            return False  # Stop execution BEFORE cooldown is applied
    user_last_command[user] = item  # --- Store Last Command for Anti-Spam Enforcement ---
    if user not in user_cooldowns:  # --- Apply Cooldown for This User & Category ---
        user_cooldowns[user] = {}
    if category not in user_cooldowns[user]:  # Only apply if no active cooldown exists
        user_cooldowns[user][category] = time.time() + cooldown_time
    if category not in category_cooldowns:  # --- Apply Global Category Cooldown (only if not set already) ---
        category_cooldowns[category] = time.time() + cooldown_time
    return True  # Cooldown successfully applied
def remove_expired_item_cooldowns():    # Remove expired cooldowns from the tracker without affecting active ones
    current_time = time.time()
    for user in list(user_cooldowns.keys()):    # Remove expired per-user cooldowns
        expired_categories = [category for category in user_cooldowns[user] if current_time >= user_cooldowns[user][category]]
        for category in expired_categories:
            del user_cooldowns[user][category]
        if not user_cooldowns[user]:  # Remove user if all their cooldowns expired
            del user_cooldowns[user]
    expired_categories = [category for category in category_cooldowns if current_time >= category_cooldowns[category]]  # Remove expired global category cooldowns
    for category in expired_categories:
        del category_cooldowns[category]
def give_command(message, user):    #Handle item giving with category cooldown enforcement first
    remove_expired_item_cooldowns()  # Clean expired cooldowns
    command_parts = message.split(maxsplit=1)
    if len(command_parts) < 2:
        minescript.echo(f"{user}, please specify an item. Usage: !give <item> <count>")
        return
    item_details = command_parts[1].split()
    item = item_details[0]
    try:    # --- Ensure valid quantity ---
        quantity = int(item_details[1]) if len(item_details) > 1 else 1
    except ValueError:
        quantity = 1  # Default to 1 if conversion fails
    quantity = max(1, min(8, quantity))  # Enforce min 1, max 8
    category = get_item_category(item)  # Get item category
    if category not in item_cooldown_times: # Debugging: Check if category is valid before using it
        minescript.echo(f"Error: Category '{category}' not found in cooldown_times.")
        return
    if not apply_item_cooldown(user, item): # --- Apply Category Cooldown FIRST ---
        return  # Stop execution if cooldown is active
    threading.Thread(target=lambda: process_give_command(item, quantity, user), daemon=True).start()    # --- Execute the command in a separate thread ---
def process_give_command(item, quantity, user): #Handles the actual /give command execution
    category = get_item_category(item)  # Ensure single-stack categories always give only 1 item
    if category in ["uncommon_single_stack", "rare_single_stack", "epic_single_stack", "common_single_stack",
                    "admin", "leather", "iron", "gold", "diamond", "netherite"]:
        quantity = 1
    minescript.execute(f"/give @p {item} {quantity}")   # Execute give command
    minescript.echo(f"{user} gave {quantity} {item}(s)")

############################################################################################################

restricted_mobs = ["wither", "ender_dragon"]    # --- Category Definitions ---
passive_mobs = [
    "allay", "armadillo", "axolotl", "bat", "camel", "cat", "chicken", "cod", "cow", "donkey",
    "frog", "glow_squid", "horse", "mooshroom", "mule", "ocelot", "parrot", "pig", "pufferfish",
    "rabbit", "salmon", "sheep", "skeleton_horse", "sniffer", "snow_golem", "squid", "strider",
    "tadpole", "tropical_fish", "turtle", "villager", "wandering_trader"
]
neutral_mobs = [
    "bee", "cave_spider", "dolphin", "drowned", "enderman", "fox", "goat", "iron_golem",
    "llama", "panda", "piglin", "polar_bear", "spider", "trader_llama", "wolf", "zombified_piglin"
]
hostile_mobs = [
    "blaze", "breeze", "creaking", "endermite", "evoker", "guardian",
    "hoglin", "husk", "magma_cube", "phantom", "zoglin", "pillager", "shulker",
    "silverfish", "skeleton", "slime", "stray", "vex", "zombie", "zombie_villager"
]
super_hostile_mobs = [
    "bogged", "ravager", "wither_skeleton", "piglin_brute", "vindicator", "elder_guardian",
    "warden", "ghast", "creeper"
]
special_mobs = {
    "killer_rabbit": "/summon rabbit ~ ~ ~ {RabbitType:99}",
    "johnny": "/summon vindicator ~ ~ ~ {CustomName:'{\"text\":\"Johnny\"}',CustomNameVisible:1}",
    "toast": "/summon rabbit ~ ~ ~ {CustomName:'{\"text\":\"Toast\"}',CustomNameVisible:1}",
    "jeb_sheep": "/summon sheep ~ ~ ~ {CustomName:'{\"text\":\"jeb_\"}',CustomNameVisible:1}",
    "giant": "/summon giant",
    "zombie_horse": "/summon zombie_horse",
    "illusioner": "/summon illusioner",
    "spawner_minecart": "/summon spawner_minecart",
    "charged_creeper": "/summon creeper ~ ~ ~ {powered:true,fuse:80}",
    "tnt": "/summon tnt ~ ~ ~ {fuse:80}"
}
def get_mob_category(mob):
    """Determine the category of a mob based on predefined classifications."""
    if mob in restricted_mobs:
        return "restricted"
    if mob in passive_mobs:
        return "passive"
    if mob in neutral_mobs:
        return "neutral"
    if mob in hostile_mobs:
        return "hostile"
    if mob in super_hostile_mobs:
        return "super_hostile"
    if mob in special_mobs:
        return "special_passive" if mob in ["zombie_horse", "spawner_minecart", "toast", "jeb_sheep"] else "special_hostile"
    return "unknown"
mob_cooldown_times = {  # --- Cooldown Times (in seconds) ---
    "passive": 2.5,
    "neutral": 5,
    "hostile": 20,
    "super_hostile": 120,
    "special_passive": 2.5,
    "special_hostile": 120,
}
def apply_mob_cooldown(user, mob):  # Apply cooldown to an entire category per user while ensuring category-wide enforcement
    category = get_mob_category(mob)
    if category == "restricted":    # --- Restriction Check ---
        minescript.echo(f"{user}, the entity '{mob}' is restricted! Please choose a different mob to summon.")
        return False
    remove_expired_mob_cooldowns()  # --- Remove expired cooldowns BEFORE checking new ones ---
    if category in ["hostile", "super_hostile", "special_hostile"]: # --- Overall Hostile Summon Cooldown (5s default, 30s for debugging) ---
        remaining_time = user_hostile_cooldowns.get(user, 0) - time.time()
        if remaining_time > 0:
            minescript.echo(f"{user}, you must wait {round(remaining_time, 1)} more seconds before summoning another hostile mob!")
            return False  # ⬅️ **STOP EXECUTION IMMEDIATELY**
        user_hostile_cooldowns[user] = time.time() + 7  # ⬅️ Adjust to 5s after debugging
    if category not in mob_cooldown_times:  # Ensure category exists in mob_cooldown_times
        minescript.echo(f"Error: Category '{category}' not found in mob_cooldown_times.")
        return False
    cooldown_time = mob_cooldown_times[category]  # Safe to access now
    if user_last_summon.get(user) == mob:   # --- Prevent users from summoning the same mob twice in a row ---
        minescript.echo(f"{user}, you cannot summon {mob} twice in a row!")
        return False  # Stop execution BEFORE cooldown is applied
    if user in user_summon_cooldowns and category in user_summon_cooldowns[user]:   # --- Prevent users from summoning different mobs in the same category while on cooldown ---
        remaining_time = round(user_summon_cooldowns[user][category] - time.time(), 1)
        if remaining_time > 0:
            minescript.echo(f"{user}, you must wait {remaining_time} seconds before summoning another {category} mob!")
            return False  # Stop execution BEFORE cooldown is applied
    if category in category_cooldowns:  # --- Prevent global category spam ---
        remaining_time = round(category_cooldowns[category] - time.time(), 1)
        if remaining_time > 0:
            minescript.echo(f"{user}, the {category} category is on cooldown for {remaining_time} more seconds!")
            return False  # Stop execution BEFORE cooldown is applied
    user_last_summon[user] = mob    # --- Store Last Summoned Mob for Anti-Spam Enforcement ---
    if user not in user_summon_cooldowns:   # --- Apply Cooldown for This User & Category ---
        user_summon_cooldowns[user] = {}
    user_summon_cooldowns[user][category] = time.time() + cooldown_time  # Ensures category cooldown applies
    if category not in category_cooldowns:  # --- Apply Global Category Cooldown (only if not set already) ---
        category_cooldowns[category] = time.time() + cooldown_time
    return True  # Cooldown successfully applied
def remove_expired_mob_cooldowns(): # Remove expired cooldowns from the tracker without affecting active ones
    current_time = time.time()
    for user in list(user_summon_cooldowns.keys()): # Remove expired per-user cooldowns
        expired_categories = [category for category in user_summon_cooldowns[user] 
                              if current_time >= user_summon_cooldowns[user][category]]
        for category in expired_categories:
            del user_summon_cooldowns[user][category]
        if not user_summon_cooldowns[user]:  # Remove user if all their cooldowns expired
            del user_summon_cooldowns[user]
    expired_categories = [category for category in category_cooldowns   # Remove expired global category cooldowns
                          if current_time >= category_cooldowns[category]]
    for category in expired_categories:
        del category_cooldowns[category]
    for user in list(user_hostile_cooldowns.keys()):    # Remove expired hostile cooldowns per user
        if current_time >= user_hostile_cooldowns[user]:  
            del user_hostile_cooldowns[user]
def summon_command(message, user):  # --- Summon Command ---
    command_parts = message.split()
    if len(command_parts) < 2:
        minescript.echo(f"{user}, please specify a mob to summon. Usage: !summon <mob>")
        return
    mob = command_parts[1].lower()
    remove_expired_mob_cooldowns()
    if not apply_mob_cooldown(user, mob):
        return
    def execute_summon():
        try:
            minescript.execute(special_mobs[mob] if mob in special_mobs else f"/summon minecraft:{mob}")
            minescript.echo(f"{user} summoned a {'special ' if mob in special_mobs else ''}{mob}!")
        except Exception as e:
            minescript.echo(f"Failed to summon. Error: {str(e)}")
    threading.Thread(target=execute_summon, daemon=True).start()

############################################################################################################

weather_conditions = {  # Dictionary to map weather conditions to the corresponding action
    "clear": "/weather clear",
    "rain": "/weather rain",
    "thunder": "/weather thunder"
}
weather_cooldown_times = {  # Cooldown durations for each weather condition (adjust as needed)
    "clear": 2.5,   # 2.5 seconds cooldown for clear
    "rain": 5,      # 5 seconds cooldown for rain
    "thunder": 20   # 20 seconds cooldown for thunder
}
def weather_command(message, user): # Function to process the weather command in chat
    global user_cooldowns
    command_parts = message.split() # Extract the weather condition after '!weather'
    if len(command_parts) <= 1:  # If there's no condition provided
        minescript.echo(f"{user}, please specify a weather condition after !weather, <clear, rain, thunder>")
        return
    weather_condition = command_parts[1].lower()
    if weather_condition not in weather_conditions: # Check if the condition is valid (clear, rain, thunder)
        minescript.echo(f"{user}, '{weather_condition}' is not a valid weather condition. Use !weather <clear, rain, thunder>.")
        return
    if user not in user_cooldowns:  # Initialize user cooldowns if not present
        user_cooldowns[user] = {"last_used_time": 0, "current_cooldown": 0}
    last_used_time = user_cooldowns[user]["last_used_time"] # Get the last used time and the cooldown for the selected weather condition
    current_time = time.time()
    cooldown_time = weather_cooldown_times[weather_condition]
    if current_time - last_used_time < user_cooldowns[user]["current_cooldown"]:    # Check if the cooldown for the most recent weather condition has expired
        remaining_time = int(user_cooldowns[user]["current_cooldown"] - (current_time - last_used_time))
        minescript.echo(f"{user}, you must wait {remaining_time} seconds before changing the weather again.")
        return
    minescript.execute(weather_conditions[weather_condition])   # Execute the corresponding weather command
    minescript.echo(f"{user} made it {weather_condition}!")
    user_cooldowns[user]["last_used_time"] = current_time   # Update the last used time and set the cooldown based on the longest cooldown for the selected weather condition
    user_cooldowns[user]["current_cooldown"] = max(cooldown_time, user_cooldowns[user]["current_cooldown"])

############################################################################################################

difficulty_conditions = {   # Dictionary to map difficulty conditions to the corresponding action
    "peaceful": "/difficulty peaceful",
    "easy": "/difficulty easy",
    "normal": "/difficulty normal",
    "hard": "/difficulty hard"
}
difficulty_cooldown_times = {   # Cooldown durations for each difficulty condition (adjust as needed)
    "peaceful": 7.5,   # 25 seconds cooldown for peaceful
    "easy": 5,        # 50 seconds cooldown for easy
    "normal": 7.5,     # 100 seconds cooldown for normal
    "hard": 10        # 150 seconds cooldown for hard
}
def difficulty_command(message, user):  # Function to process the difficulty command in chat
    global user_cooldowns
    command_parts = message.split() # Extract the difficulty condition after '!difficulty'
    if len(command_parts) <= 1:  # If no difficulty condition provided
        minescript.echo(f"{user}, please specify a difficulty level after '!difficulty'.\nValid conditions are: peaceful, easy, normal, hard.")
        return
    difficulty_condition = command_parts[1].lower()
    if difficulty_condition not in difficulty_conditions:   # Check if the condition is valid (peaceful, easy, normal, hard)
        minescript.echo(f"{user}, '{difficulty_condition}' is not a valid difficulty level.\nUse '!difficulty' followed by one of the following: peaceful, easy, normal, hard.")
        return
    if user not in user_cooldowns:  # Initialize user cooldowns if not present
        user_cooldowns[user] = {"last_used_time": 0, "current_cooldown": 0}
    last_used_time = user_cooldowns[user]["last_used_time"] # Get the last used time and the cooldown for the selected difficulty
    current_time = time.time()
    cooldown_time = difficulty_cooldown_times[difficulty_condition]
    if current_time - last_used_time < user_cooldowns[user]["current_cooldown"]:    # Check if the cooldown for the most recent difficulty has expired
        remaining_time = int(user_cooldowns[user]["current_cooldown"] - (current_time - last_used_time))
        minescript.echo(f"{user}, you must wait {remaining_time} seconds before changing the difficulty again.")
        return
    minescript.execute(difficulty_conditions[difficulty_condition]) # Execute the corresponding difficulty command
    minescript.echo(f"{user} set the difficulty to {difficulty_condition}!")
    user_cooldowns[user]["last_used_time"] = current_time   # Update the last used time and set the cooldown based on the longest cooldown for the selected difficulty
    user_cooldowns[user]["current_cooldown"] = max(cooldown_time, user_cooldowns[user]["current_cooldown"])

############################################################################################################

def gravity_command(message, user):
    global user_last_command
    command_parts = message.split()
    if len(command_parts) < 2:
        minescript.echo(f"{user}, please specify a gravity type. Usage: !gravity <space/moon/jupiter/extreme/blackhole>")
        return
    gravity_type = command_parts[1].lower()  # Extract the gravity type
    gravity_settings = {    # Define gravity settings
        "space": {
            "commands": ["/attribute @p minecraft:generic.gravity base set 0.0",],
            "duration": 10,
            "cooldown": 5
        },
        "moon": {
            "commands": [
                "/attribute @p minecraft:generic.movement_speed base set 0.08",
                "/attribute @p minecraft:generic.gravity base set 0.0133",
                "/attribute @p minecraft:generic.fall_damage_multiplier base set 0"
            ],
            "duration": 15,
            "cooldown": 5
        },
        "jupiter": {
            "commands": [
                "/attribute @p minecraft:generic.movement_speed base set 0.04",
                "/attribute @p minecraft:generic.gravity base set 0.2",
                "/execute as @e at @s run tp @s ~ ~-1 ~"
            ],
            "duration": 10,
            "cooldown": 10
        },
        "extreme": {
            "commands": [
                "/attribute @p minecraft:generic.movement_speed base set 0.02",
                "/attribute @p minecraft:generic.gravity base set 0.8",
                "/execute as @e at @s run tp @s ~ ~-1 ~"
            ],
            "duration": 7,
            "cooldown": 20
        },
        "blackhole": {
            "commands": [
                "/attribute @p minecraft:generic.movement_speed base set 0.01",
                "/attribute @p minecraft:generic.gravity base set 1.0",
                "/attribute @p minecraft:generic.jump_strength base set 0",
                "/effect give @p darkness 5 1 true",
                "/effect give @e wither 5 1 true",
                "/execute as @e at @s run tp @s ~ ~-2 ~"
            ],
            "duration": 5,
            "cooldown": 120
        }
    }
    if gravity_type not in gravity_settings:
        minescript.echo(f"{user}, invalid gravity type. Choose from: space, moon, jupiter, extreme, blackhole.")
        return
    if user in user_last_command and user_last_command[user] == "!gravity": # Global Anti-Spam Check (Prevents immediate re-use of !gravity in any form)
        minescript.echo(f"{user}, you must use a different command before using !gravity again!")
        return
    settings = gravity_settings[gravity_type]
    commands = settings["commands"]
    duration = settings["duration"]
    cooldown_time = settings["cooldown"]
    def execute_gravity():
        """Executes the gravity effect and resets it after the duration."""
        global user_last_command
        try:
            for command in commands:
                minescript.execute(command)
            minescript.echo(f"{user} activated {gravity_type} gravity for {duration} seconds!")
            time.sleep(duration)
            minescript.execute("/attribute @p minecraft:generic.movement_speed base set 0.10000000149011612")
            minescript.execute("/attribute @p minecraft:generic.gravity base set 0.08")
            minescript.execute("/attribute @p minecraft:generic.jump_strength base set 0.41999998688697815")
            minescript.execute("/attribute @p minecraft:generic.fall_damage_multiplier base set 1")
            time.sleep(0.5)
            minescript.echo(f"Gravity reset to normal.")
        except Exception as e:
            minescript.echo(f"Failed to change gravity. Error: {str(e)}")
        user_last_command[user] = "!gravity"
    execute_with_cooldown(user, "!gravity", cooldown_time, execute_gravity)

############################################################################################################

def speed_command(message, user):   # Handles the speed command with cooldowns and validation
    global user_last_command
    command_parts = message.split()
    if len(command_parts) < 2:
        minescript.echo(f"{user}, please specify a speed level. Usage: !speed <level>")
        return
    speed_level = command_parts[1].lower()
    speed_settings = {
        "frozen": (0, 7, 40),
        "snail": (0.01, 7, 15),
        "turtle": (0.02, 10, 10),
        "sloth": (0.03, 15, 7),
        "koala": (0.05, 20, 5),
        "super": (1, 20, 10),
        "sonic": (2.5, 15, 7),
        "hyper": (5, 10, 10),
        "light": (10, 7, 15),
        "beyond": (20, 5, 20)
    }
    if speed_level not in speed_settings:
        minescript.echo(f"{user}, invalid speed level. Choose from: " + ", ".join(speed_settings.keys()))
        return
    speed_value, duration, cooldown = speed_settings[speed_level]
    if user in user_last_command and user_last_command[user] == "!speed":   # Global Anti-Spam Check
        minescript.echo(f"{user}, you must use a different command before using !speed again!")
        return
    def execute_speed():    #Executes the speed change logic after cooldown check
        global user_last_command
        try:
            minescript.execute(f"/attribute @p minecraft:generic.movement_speed base set {speed_value}")
            minescript.echo(f"{user} set their speed to {speed_level} for {duration} seconds!")
            time.sleep(duration)
            minescript.execute(f"/attribute @p minecraft:generic.movement_speed base set 0.10000000149011612")
            minescript.echo("Your speed has been reset to normal.")
        except Exception as e:
            minescript.echo(f"Failed to change speed. Error: {str(e)}")
        user_last_command[user] = "!speed"
    execute_with_cooldown(user, "!speed", cooldown, execute_speed)

############################################################################################################

def damage_command(message, user):
    global user_last_command
    command_parts = message.split()
    if len(command_parts) < 2:
        minescript.echo(f"{user}, please specify a damage level. Usage: !damage <level>")
        return
    damage_level = command_parts[1].lower()
    damage_settings = {
        "1": (1, 12),
        "quarter": (5, 60),
        "half": (10, 120),
        "onehit": (1, 240)  # Special case for health alteration
    }
    if damage_level not in damage_settings:
        minescript.echo(f"{user}, invalid damage level. Choose from: " + ", ".join(damage_settings.keys()))
        return
    damage_value, cooldown = damage_settings[damage_level]
    if user in user_last_command and user_last_command[user] == "!damage":  # Global Anti-Spam Check
        minescript.echo(f"{user}, you must use a different command before using !damage again!")
        return
    def execute_damage():   # Executes the damage logic after cooldown check
        global user_last_command
        try:
            if damage_level == "onehit":
                minescript.execute("/attribute @p minecraft:generic.max_health base set 1")
                minescript.echo(f"{user} set their health to 1 for 15 seconds!")
                time.sleep(15)
                minescript.execute("/attribute @p minecraft:generic.max_health base set 20")
                minescript.execute("/effect give @p minecraft:instant_health 1 3")
                minescript.echo("Your health has been restored to normal.")
            else:
                minescript.execute(f"/damage @p {damage_value}")
                minescript.echo(f"{user} took {damage_value} damage!")
        except Exception as e:
            minescript.echo(f"Failed to apply damage. Error: {str(e)}")
        user_last_command[user] = "!damage"
    execute_with_cooldown(user, "!damage", cooldown, execute_damage)

############################################################################################################

def heal_command(message, user):
    global user_last_command
    command_parts = message.split()
    if len(command_parts) < 2:
        minescript.echo(f"{user}, please specify a healing level. Usage: !heal <level>")
        return
    heal_level = command_parts[1].lower()
    heal_settings = {
        "1": (3, "regeneration 1 2 true"),
        "quarter": (15, "regeneration 1 4 true"),
        "half": (30, "regeneration 2 4 true"),
        "full": (60, "minecraft:instant_health 1 3")
    }
    if heal_level not in heal_settings:
        minescript.echo(f"{user}, invalid healing level. Choose from: " + ", ".join(heal_settings.keys()))
        return
    heal_time, effect_command = heal_settings[heal_level]
    if user in user_last_command and user_last_command[user] == "!heal":    # Global Anti-Spam Check
        minescript.echo(f"{user}, you must use a different command before using !heal again!")
        return
    def execute_heal(): # Executes the healing logic after cooldown check
        global user_last_command
        try:
            minescript.execute(f"/effect give @p {effect_command}")
            minescript.echo(f"{user} healed with {heal_level} level!")
        except Exception as e:
            minescript.echo(f"Failed to apply healing. Error: {str(e)}")
        user_last_command[user] = "!heal"
    execute_with_cooldown(user, "!heal", heal_time, execute_heal)

############################################################################################################

def hunger_command(message, user):
    global user_last_command
    command_parts = message.split()
    if len(command_parts) < 2:
        minescript.echo(f"{user}, please specify a hunger level. Usage: !hunger <level>")
        return
    hunger_level = command_parts[1].lower()
    hunger_settings = {
        "1": (6, "hunger 1 39 true"),
        "quarter": (30, "hunger 1 200 true"),
        "half": (60, "hunger 2 200 true"),
        "max": (120, "hunger 7 255 true")
    }
    if hunger_level not in hunger_settings:
        minescript.echo(f"{user}, invalid hunger level. Choose from: " + ", ".join(hunger_settings.keys()))
        return
    hunger_time, effect_command = hunger_settings[hunger_level]
    if user in user_last_command and user_last_command[user] == "!hunger":  # Global Anti-Spam Check
        minescript.echo(f"{user}, you must use a different command before using !hunger again!")
        return
    def execute_hunger():   # Executes the hunger logic after cooldown check
        global user_last_command
        try:
            minescript.execute(f"/effect give @p {effect_command}")
            minescript.echo(f"{user} set their hunger to {hunger_level} level!")
        except Exception as e:
            minescript.echo(f"Failed to apply hunger. Error: {str(e)}")
        user_last_command[user] = "!hunger"
    execute_with_cooldown(user, "!hunger", hunger_time, execute_hunger)

############################################################################################################

def feed_command(message, user):
    global user_last_command
    command_parts = message.split()
    if len(command_parts) < 2:
        minescript.echo(f"{user}, please specify a feed level. Usage: !feed <level>")
        return
    feed_level = command_parts[1].lower()
    feed_settings = {
        "1": (2.5, "saturation 1 1 true"),
        "quarter": (5, "saturation 1 4 true"),
        "half": (10, "saturation 1 9 true"),
        "full": (20, "saturation 1 255 true")
    }
    if feed_level not in feed_settings:
        minescript.echo(f"{user}, invalid feed level. Choose from: " + ", ".join(feed_settings.keys()))
        return
    feed_time, effect_command = feed_settings[feed_level]
    if user in user_last_command and user_last_command[user] == "!feed":    # Global Anti-Spam Check
        minescript.echo(f"{user}, you must use a different command before using !feed again!")
        return
    def execute_feed(): # Executes the feed logic after cooldown check
        global user_last_command
        try:
            minescript.execute(f"/effect give @p {effect_command}")
            minescript.echo(f"{user} fed with {feed_level} level!")
        except Exception as e:
            minescript.echo(f"Failed to apply feed. Error: {str(e)}")
        user_last_command[user] = "!feed"
    execute_with_cooldown(user, "!feed", feed_time, execute_feed)

############################################################################################################

def nojump_command(message, user):
    global user_last_command
    command_parts = message.split()
    if user in user_last_command and user_last_command[user] == "!nojump":  # Anti-Spam Check
        minescript.echo(f"{user}, you must use a different command before using !nojump again!")
        return
    def execute_nojump():   # Disables jumping for 30 second
        global user_last_command
        try:
            if '!nojump' in command_parts:
                # Send feedback and disable jumping
                minescript.echo(f"{user} has disabled jumping for 30 seconds!")
                minescript.execute("/gamerule sendCommandFeedback false")
                start_time = time.time()
                last_position = minescript.player_position()  # Initial position as [x, y, z]
                while time.time() - start_time < 30:  # Run for 30 seconds
                    current_position = minescript.player_position()
                    x, y, z = current_position
                    if y > last_position[1] + 0.5:  # Jump detected (Y increase beyond threshold)   # Allow small increases in Y for slopes or stairs, but restrict large jumps
                        minescript.execute(f"/tp @p {last_position[0]} {last_position[1]} {last_position[2]}")
                        minescript.echo("Jumping is disabled!")  # Optional feedback for players
                    else:
                        last_position = current_position  # Update the last known position
                    time.sleep(0.1)  # Check every 0.1 seconds for smooth restriction
                minescript.execute("/gamerule sendCommandFeedback true")    # Enable jumping again after 30 seconds
                minescript.echo("Jumping is now enabled again!")
                time.sleep(15)  # Adding a short wait time between executions to avoid spam
            user_last_command[user] = "!nojump" # Update last command timestamp to prevent rapid reuse
        except Exception as e:
            minescript.echo(f"Failed to disable jumping. Error: {str(e)}")
    execute_with_cooldown(user, "!nojump", 30, execute_nojump)  # Global cooldown for command reuse

############################################################################################################

def scramble_command(message, user):
    global user_last_command
    command_parts = message.split()
    if user in user_last_command and user_last_command[user] == "!scramble":    # Global Anti-Spam Check
        minescript.echo(f"{user}, you must use a different command before using !scramble again!")
        return
    def execute_scramble(): # Executes the inventory scramble logic after cooldown check
        global user_last_command
        try:
            minescript.echo(f"{user} has scrambled your inventory!")    # Notify players about the scramble
            inventory = minescript.player_inventory()   # Fetch the player's inventory
            if inventory:
                all_slots = [item.slot for item in inventory]   # Get all inventory slots
                if len(all_slots) > 1:  # Ensure there are enough items to scramble
                    for _ in range(len(all_slots) * 2):  # Perform multiple swaps for better scrambling
                        slot_a, slot_b = random.sample(all_slots, 2)    # Randomly select two distinct slots
                        if slot_a < 9 and slot_b >= 9:  # If slot_a is in hotbar and slot_b in main inventory
                            hotbar_slot = minescript.player_inventory_slot_to_hotbar(slot_b)    # Swap item from inventory to hotbar
                            minescript.player_inventory_select_slot(slot_a)
                            minescript.player_inventory_select_slot(hotbar_slot)
                        elif slot_a >= 9 and slot_b < 9:  # If slot_a is in main inventory and slot_b in hotbar
                            hotbar_slot = minescript.player_inventory_slot_to_hotbar(slot_a)    # Swap item from inventory to hotbar
                            minescript.player_inventory_select_slot(slot_b)
                            minescript.player_inventory_select_slot(hotbar_slot)
                        elif slot_a >= 9 and slot_b >= 9:  # Both slots in main inventory
                            hotbar_slot_a = minescript.player_inventory_slot_to_hotbar(slot_a)  # Swap each to the hotbar temporarily
                            hotbar_slot_b = minescript.player_inventory_slot_to_hotbar(slot_b)
                            minescript.player_inventory_select_slot(hotbar_slot_a)  # Swap hotbar slots
                            minescript.player_inventory_select_slot(hotbar_slot_b)
                        else:  # Both slots in hotbar
                            prev_slot_a = minescript.player_inventory_select_slot(slot_a)   # Simply swap the hotbar slots
                            prev_slot_b = minescript.player_inventory_select_slot(slot_b)
                            minescript.player_inventory_select_slot(prev_slot_a)
                            minescript.player_inventory_select_slot(prev_slot_b)
                            time.sleep(15)
                    minescript.echo("Your inventory has been scrambled!")  # Notify completion
                else:
                    minescript.echo("Not enough items in the inventory to scramble!")  # Handle edge cases
            else:
                minescript.echo("Failed to retrieve inventory!")  # Handle potential errors
        except Exception as e:
            minescript.echo(f"Failed to execute scramble. Error: {str(e)}")
        user_last_command[user] = "!scramble"
    execute_with_cooldown(user, "!scramble", 30, execute_scramble)  # 30 seconds cooldown for the scramble command

############################################################################################################

def drop_command(message, user):
    global user_last_command
    command_parts = message.split()
    if user in user_last_command and user_last_command[user] == "!drop":    # Global Anti-Spam Check
        minescript.echo(f"{user}, you must use a different command before using !drop again!")
        return
    def execute_drop_item():
        try:
            minescript.press_key_bind("key.drop", True)
            minescript.press_key_bind("key.drop", False)
            minescript.echo(f"{user} dropped your item")
        except Exception as e:
            minescript.echo(f"Failed to drop item. Error: {str(e)}")
    def execute_drop_all():
        try:
            minescript.echo(f"{user} dropped all your items!")
            inventory = minescript.player_inventory()   # Fetch the player's inventory
            if inventory:
                all_slots = [item.slot for item in inventory]   # Get all inventory slots
                row_size = 9  # Typically, Minecraft's hotbar is 9 slots    # Define row size and number of rows to transfer
                max_rows = 4  # Number of rows to transfer
                rows_transferred = 0
                while rows_transferred < max_rows:  # Step 1: Drop all items in the hotbar for each row
                    pyautogui.keyDown('ctrl')  # Hold down Ctrl for mass dropping   # Drop items from the hotbar
                    for hotbar_slot in range(row_size):  # Hotbar slots are typically 0-8
                        minescript.player_inventory_select_slot(hotbar_slot)
                        minescript.press_key_bind("key.drop", True)  # Press Q to drop the item stack
                        minescript.execute("/execute at @p run execute as @e[type=item, distance=..10] run data merge entity @s {PickupDelay:200}")
                        time.sleep(0.05)  # Add delay to ensure the item is dropped
                    pyautogui.keyUp('ctrl')
                    for i in range(row_size):   # Step 2: Transfer the next row of items from the main inventory to the hotbar
                        main_slot = rows_transferred * row_size + 9 + i  # Calculate main inventory slot index
                        if main_slot >= len(all_slots):  # Stop transferring if inventory is empty
                            break
                        hotbar_slot = minescript.player_inventory_slot_to_hotbar(main_slot) # Transfer item from main inventory to corresponding hotbar slot
                        if hotbar_slot is not None:  # Ensure valid hotbar slot
                            minescript.player_inventory_select_slot(main_slot)
                            minescript.player_inventory_select_slot(hotbar_slot)
                            time.sleep(0.025)  # Add delay to ensure smooth transfer
                    rows_transferred += 1   # Increment rows transferred
                shield_slot = 40  # Off-hand slot   # Step 2.5: Drop the shield from the off-hand (slot 40) if equipped
                minescript.player_inventory_select_slot(shield_slot)
                minescript.press_key_bind("key.swapOffhand", True)  # Swap shield from off-hand to main hand (if it's equipped)
                minescript.press_key_bind("key.drop", True)  # Drop the shield
                minescript.execute("/execute at @p run execute as @e[type=item, distance=..10] run data merge entity @s {PickupDelay:200}")
                time.sleep(0.05)  # Ensure shield drop action completes
                for armor_slot in ["armor.head", "armor.chest", "armor.legs", "armor.feet"]:    # Step 3: Drop equipped armor
                    minescript.execute(f"/execute at @p run item replace entity @p weapon.mainhand from entity @p {armor_slot}")
                    minescript.press_key_bind("key.drop", True)
                    minescript.execute(f"/execute at @p run item replace entity @p {armor_slot} with air")
                    minescript.execute("/execute at @p run execute as @e[type=item, distance=..10] run data merge entity @s {PickupDelay:200}")
                    time.sleep(0.05)  # Add delay for each armor piece drop
                minescript.press_key_bind("key.drop", False)
            else:
                minescript.echo("Failed to retrieve inventory!")
        except Exception as e:
            minescript.echo(f"Failed to drop all items. Error: {str(e)}")
    if "!drop item" in message:
        execute_with_cooldown(user, "!drop item", 10, execute_drop_item)  # 30 seconds cooldown for dropping one item
    if "!drop all" in message:
        execute_with_cooldown(user, "!drop all", 60, execute_drop_all)  # 60 seconds cooldown for dropping all items

############################################################################################################

def effect_command(message, user):
    command_parts = message.split() # Split the message to extract effect and amplifier
    effect_data = { # Define the effect categories and their cooldowns
        "super_positive": {
            "effects": ["hero_of_the_village", "dolphins_grace", "conduit_power"],
            "cooldown_time": 30  # 30 seconds cooldown
        },
        "positive": {
            "effects": ["haste", "strength", "jump_boost", "water_breathing", "invisibility", "night_vision", "slow_falling", "luck"],
            "cooldown_time": 15  # 15 seconds cooldown
        },
        "negative": {
            "effects": ["slowness", "mining_fatigue", "nausea", "blindness", "weakness", "bad_omen", "darkness", "glowing", "unluck"],
            "cooldown_time": 30  # 30 seconds cooldown
        },
        "super_negative": {
            "effects": ["poison"],
            "cooldown_time": 120  # 120 seconds cooldown
        },
        "duration": 10  # Shared duration for all effects
    }
    def execute_effect(effect, amplifier, duration):    # Function to execute the effect command
        try:
            minescript.execute(f"/effect give @p {effect} {duration} {amplifier} true")
            minescript.echo(f"{user} gave you the effect {effect} with amplifier {amplifier} for {duration} seconds.")  # Notify the player
        except Exception as e:
            minescript.echo(f"Failed to apply effect. Error: {str(e)}")
    if len(command_parts) > 2:  # Check if the message has at least two parts (effect and amplifier)
        effect = command_parts[1].lower()  # Extract the effect name
        amplifier = None
        effect_found = False    # Validate if the effect belongs to one of the defined categories
        cooldown_time = 0
        for category, data in effect_data.items():
            if isinstance(data, dict):  # Make sure the value is a dictionary before checking
                effects = data.get("effects", [])
                if effect in effects:  # Check if the effect is in the list
                    effect_found = True
                    cooldown_time = data["cooldown_time"]
                    break
        if not effect_found:
            valid_effects = []  # List all valid effects from all categories
            for data in effect_data.values():
                if isinstance(data, dict):  # Ensure we're only working with dictionaries
                    valid_effects.extend(data.get("effects", []))
            minescript.echo(f"{user}, the effect '{effect}' is invalid. Here are the valid effects: {', '.join(valid_effects)}")
            return
        try:    # Handle amplifier input
            amplifier = int(command_parts[2])  # Extract and validate amplifier
            if amplifier < 1 or amplifier > 5:  # Ensure amplifier is within the valid range
                raise ValueError("Amplifier out of range")
        except ValueError:
            minescript.echo(f"{user}, please provide a valid amplifier (1-5). Usage: !effect <effect> <amplifier>")
            return
        if execute_with_cooldown(user, "!effect", cooldown_time, lambda: execute_effect(effect, amplifier, effect_data["duration"])):   # Check cooldown and execute the effect command
            minescript.echo(f"{user}, please wait before using !effect again.")
            return
    else:
        minescript.echo(f"{user}, please specify an effect and amplifier. Usage: !effect <effect> <amplifier>") # Notify the user if the command is incomplete

############################################################################################################

enchant_cooldowns = {   # Cooldown times for positive and curse enchantments
    "positive": 15,  # 15 seconds for positive enchantments
    "curse": 30      # 30 seconds for curses
}
enchantments = {    # Enchantment categories (positive and curse)
    "positive": [
        "bane_of_arthropods", "breach", "cleaving", "density", "efficiency", "fire_aspect",
        "flame", "fortune", "impaling", "infinity", "knockback", "looting", "loyalty",
        "luck_of_the_sea", "lure", "mending", "multishot", "piercing", "power", "punch",
        "quick_charge", "riptide", "sharpness", "silk_touch", "smite", "sweeping",
        "unbreaking", "wind_burst", "aqua_affinity", "blast_protection", "depth_strider",
        "feather_falling", "fire_protection", "frost_walker", "projectile_protection", "protection",
        "respiration", "soul_speed", "swift_sneak", "thorns"
    ],
    "curse": [
        "binding_curse", "vanishing_curse"
    ]
}
def enchant_command(message, user): # Function to process the !enchant command
    command_parts = message.split() # Split message into parts
    if len(command_parts) <= 2: # Ensure correct usage
        minescript.echo(f"{user}, please specify an enchantment and level. Usage: !enchant <enchantment> <level>")
        return
    enchantment = command_parts[1].lower()
    if enchantment in enchantments["positive"]: # Determine enchantment type
        enchantment_type = "positive"
    elif enchantment in enchantments["curse"]:
        enchantment_type = "curse"
    else:
        minescript.echo(f"{user}, '{enchantment}' is not a valid enchantment. Please choose a valid enchantment.")
        return
    try:    # Extract the level of the enchantment
        level = int(command_parts[2])  # Convert level to integer
    except ValueError:
        minescript.echo(f"{user}, please provide a valid enchantment level. Usage: !enchant <enchantment> <level>")
        return
    enchant_command = f"/enchant @p {enchantment} {level}"  # Construct the enchantment command
    execute_with_cooldown(user, "enchant", enchant_cooldowns[enchantment_type], lambda: minescript.execute(enchant_command))    # Call the execute_with_cooldown function
    minescript.echo(f"{user} enchanted your item with {enchantment} {level}.") # Notify the player

############################################################################################################

def main():
    video_id = "xjHaJSCudMs"  # Replace with your YouTube live video ID
    fetch_youtube_chat(video_id)
    minescript.echo("Finished fetching chat.")

if __name__ == "__main__":
    main()