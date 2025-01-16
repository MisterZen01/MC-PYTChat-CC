import os
import pyautogui
import pytchat
import minescript
import time
import random

# Set environment variable for the home directory
if os.name == 'nt':
    os.environ['USERPROFILE'] = os.getenv('USERPROFILE', 'C:\\Users\\Default')
else:
    os.environ['HOME'] = os.getenv('HOME', '/home/default')

# Function to fetch and process chat messages
def fetch_youtube_chat(video_id):
    try:
        minescript.echo("Starting Crowd Control...")
        minescript.execute("/gamerule sendCommandFeedback false")
        chat = pytchat.create(video_id=video_id)
        while chat.is_alive():
            for c in chat.get().sync_items():
                
                if '!screenshot' in c.message:
                    pyautogui.hotkey('f2')
                    screenshot = f"{c.author.name} took a screenshot"
                    minescript.echo(screenshot)
                    time.sleep(10)

                if '!perspective' in c.message:
                    minescript.press_key_bind("key.togglePerspective", True)
                    third = f"{c.author.name} changed your perspective"
                    minescript.echo(third)
                    time.sleep(10)

                if '!selfie' in c.message:
                    minescript.press_key_bind("key.togglePerspective", True)
                    minescript.press_key_bind("key.togglePerspective", True)
                    third = f"{c.author.name} made you look at yourself"
                    minescript.echo(third)
                    time.sleep(10)

                if '!hud' in c.message:
                    pyautogui.hotkey('f1')
                    hud = f"{c.author.name} cleared your HUD"
                    minescript.echo(hud)
                    time.sleep(10)

                if '!debug' in c.message:
                    pyautogui.hotkey('f3')
                    debug = f"{c.author.name} showed the debug screen"
                    minescript.echo(debug)
                    time.sleep(15)

                if '!attack' in c.message:
                    minescript.press_key_bind("key.attack", True)
                    minescript.press_key_bind("key.attack", False)
                    attack = f"{c.author.name} made you attack"
                    minescript.echo(attack)
                    time.sleep(10)
                
                if '!use' in c.message:
                    minescript.press_key_bind("key.use", True)
                    minescript.press_key_bind("key.use", False)
                    use = f"{c.author.name} used your item"
                    minescript.echo(use)
                    time.sleep(10)
                
                if '!pick' in c.message:
                    minescript.press_key_bind("key.pickItem", True)
                    minescript.press_key_bind("key.pickItem", False)
                    pick = f"{c.author.name} picked your block"
                    minescript.echo(pick)
                    time.sleep(10)
                
                if '!chat' in c.message:
                    minescript.press_key_bind("key.chat", True)
                    minescript.press_key_bind("key.chat", False)
                    tchat = f"{c.author.name} opened chat"
                    minescript.echo(tchat)
                    time.sleep(10)

                if '!inventory' in c.message:
                    minescript.press_key_bind("key.inventory", True)
                    minescript.press_key_bind("key.inventory", False)
                    inv = f"{c.author.name} opened your inventory"
                    minescript.echo(inv)
                    time.sleep(10)

                if '!drop item' in c.message:
                    minescript.press_key_bind("key.drop", True)
                    minescript.press_key_bind("key.drop", False)
                    drop_item = f"{c.author.name} dropped your item"
                    minescript.echo(drop_item)
                    time.sleep(10)

                if '!swap' in c.message:
                    minescript.press_key_bind("key.swapOffhand", True)
                    minescript.press_key_bind("key.swapOffhand", False)
                    swap = f"{c.author.name} made you swap items"
                    minescript.echo(swap)
                    time.sleep(10)

                if '!180' in c.message:
                    turn180 = f"{c.author.name} turned you around"
                    minescript.execute("/tp @a ~ ~ ~ ~180 ~")
                    minescript.echo(turn180)
                    time.sleep(15)

                if '!notch' in c.message:
                    notch = f"{c.author.name} gave you a Notch apple"
                    minescript.execute("/give @p minecraft:enchanted_golden_apple")
                    minescript.echo(notch)
                    time.sleep(15)

                if '!move' in c.message:
                    movement_command(c.message, c)

                if '!weather' in c.message:
                    weather_command(c.message, c)

                if '!difficulty' in c.message:
                    difficulty_command(c.message, c)

                if '!gamemode' in c.message:
                    gamemode_command(c.message, c)

                if '!summon' in c.message:
                    summon_command(c.message, c)

                if '!timeset' in c.message:
                    timeset_command(c.message, c)

                if '!slot' in c.message:
                    slot_command(c.message, c)
                
                if '!give' in c.message:
                    give_command(c.message, c)

                if '!effect' in c.message:
                    effect_command(c.message, c)

                if '!enchant' in c.message:
                    enchant_command(c.message, c)

                if '!drop all' in c.message:  # Check if the command contains "!drop all"
                    drop_all = f"{c.author.name} dropped all your items!"
                    minescript.echo(drop_all)  # Notify players about the action

                    # Fetch the player's inventory
                    inventory = minescript.player_inventory()

                    if inventory:
                        # Get all inventory slots
                        all_slots = [item.slot for item in inventory]

                        # Define row size and number of rows to transfer
                        row_size = 9  # Typically, Minecraft's hotbar is 9 slots
                        max_rows = 4  # Number of rows to transfer
                        rows_transferred = 0

                        # Step 1: Drop all items in the hotbar for each row
                        while rows_transferred < max_rows:
                            # Drop items from the hotbar
                            pyautogui.keyDown('ctrl')  # Hold down Ctrl for mass dropping
                            for hotbar_slot in range(row_size):  # Hotbar slots are typically 0-8
                                minescript.player_inventory_select_slot(hotbar_slot)
                                minescript.press_key_bind("key.drop", True)  # Press Q to drop the item stack
                                minescript.execute("/execute at @p run execute as @e[type=item, distance=..10] run data merge entity @s {PickupDelay:200}")
                                time.sleep(0.05)  # Add delay to ensure the item is dropped
                            pyautogui.keyUp('ctrl')

                            # Step 2: Transfer the next row of items from the main inventory to the hotbar
                            for i in range(row_size):
                                main_slot = rows_transferred * row_size + 9 + i  # Calculate main inventory slot index
                                if main_slot >= len(all_slots):  # Stop transferring if inventory is empty
                                    break

                                # Transfer item from main inventory to corresponding hotbar slot
                                hotbar_slot = minescript.player_inventory_slot_to_hotbar(main_slot)
                                if hotbar_slot is not None:  # Ensure valid hotbar slot
                                    minescript.player_inventory_select_slot(main_slot)
                                    minescript.player_inventory_select_slot(hotbar_slot)
                                    time.sleep(0.025)  # Add delay to ensure smooth transfer

                            # Increment rows transferred
                            rows_transferred += 1

                        # Step 2.5: Drop the shield from the off-hand (slot 40) if equipped
                        shield_slot = 40  # Off-hand slot
                        minescript.player_inventory_select_slot(shield_slot)
                        minescript.press_key_bind("key.swapOffhand", True)  # Swap shield from off-hand to main hand (if it's equipped)
                        minescript.press_key_bind("key.drop", True)  # Drop the shield
                        minescript.execute("/execute at @p run execute as @e[type=item, distance=..10] run data merge entity @s {PickupDelay:200}")
                        time.sleep(0.05)  # Ensure shield drop action completes

                        # Step 3: Drop equipped armor
                        for armor_slot in ["armor.head", "armor.chest", "armor.legs", "armor.feet"]:
                            minescript.execute(f"/execute at @p run item replace entity @p weapon.mainhand from entity @p {armor_slot}")
                            minescript.press_key_bind("key.drop", True)
                            minescript.execute(f"/execute at @p run item replace entity @p {armor_slot} with air")
                            minescript.execute("/execute at @p run execute as @e[type=item, distance=..10] run data merge entity @s {PickupDelay:200}")
                            time.sleep(0.05)  # Add delay for each armor piece drop
                        minescript.press_key_bind("key.drop", False)
                    time.sleep(30)  # Final cooldown

                if '!freeze' in c.message:
                    minescript.echo(f"{c.author.name} has froze MisterZen for 10 seconds!")
                    # Get the initial position of the local player
                    initial_position = minescript.player_position()  # Returns [x, y, z]
                    x, y, z = initial_position

                    start_time = time.time()
                    while time.time() - start_time < 15:  # Run for 10 seconds
                        # Continuously teleport the local player back to their initial position
                        minescript.execute(f"/tp @p {x} {y} {z}")
                        time.sleep(0.1)  # Repeat every 0.1 seconds for smooth enforcement
                    minescript.echo("You are now unfrozen")
                    minescript.execute("/effect give @a slow_falling 1 1 true")
                    time.sleep(15)

                if '!nojump' in c.message:
                    minescript.echo(f"{c.author.name} has disabled jumping for 30 seconds!")
                    start_time = time.time()
                    last_position = minescript.player_position()  # Initial position as [x, y, z]
                    while time.time() - start_time < 30:  # Run for 30 seconds
                        current_position = minescript.player_position()
                        x, y, z = current_position
                        # Allow small increases in Y for slopes or stairs, but restrict large jumps
                        if y > last_position[1] + 0.5:  # Jump detected (Y increase beyond threshold)
                            minescript.execute(f"/tp @p {last_position[0]} {last_position[1]} {last_position[2]}")
                            minescript.echo("Jumping is disabled!")  # Optional feedback for players
                        else:
                            last_position = current_position # Update the last known position
                        time.sleep(0.1)  # Check every 0.1 seconds for smooth restriction
                    minescript.echo("Jumping is now enabled again!")
                    time.sleep(15)

                if '!scramble' in c.message:  # Check if the command contains "!scramble"
                    scramble = f"{c.author.name} has scrambled your inventory!"
                    minescript.echo(scramble)  # Notify players about the scramble

                    # Fetch the player's inventory
                    inventory = minescript.player_inventory()
                    
                    if inventory:
                        # Get all inventory slots
                        all_slots = [item.slot for item in inventory]
                        
                        # Ensure there are enough items to scramble
                        if len(all_slots) > 1:
                            for _ in range(len(all_slots) * 2):  # Perform multiple swaps for better scrambling
                                # Randomly select two distinct slots
                                slot_a, slot_b = random.sample(all_slots, 2)
                                
                                if slot_a < 9 and slot_b >= 9:  # If slot_a is in hotbar and slot_b in main inventory
                                    # Swap item from inventory to hotbar
                                    hotbar_slot = minescript.player_inventory_slot_to_hotbar(slot_b)
                                    minescript.player_inventory_select_slot(slot_a)
                                    minescript.player_inventory_select_slot(hotbar_slot)
                                elif slot_a >= 9 and slot_b < 9:  # If slot_a is in main inventory and slot_b in hotbar
                                    # Swap item from inventory to hotbar
                                    hotbar_slot = minescript.player_inventory_slot_to_hotbar(slot_a)
                                    minescript.player_inventory_select_slot(slot_b)
                                    minescript.player_inventory_select_slot(hotbar_slot)
                                elif slot_a >= 9 and slot_b >= 9:  # Both slots in main inventory
                                    # Swap each to the hotbar temporarily
                                    hotbar_slot_a = minescript.player_inventory_slot_to_hotbar(slot_a)
                                    hotbar_slot_b = minescript.player_inventory_slot_to_hotbar(slot_b)
                                    # Swap hotbar slots
                                    minescript.player_inventory_select_slot(hotbar_slot_a)
                                    minescript.player_inventory_select_slot(hotbar_slot_b)
                                else:  # Both slots in hotbar
                                    # Simply swap the hotbar slots
                                    prev_slot_a = minescript.player_inventory_select_slot(slot_a)
                                    prev_slot_b = minescript.player_inventory_select_slot(slot_b)
                                    minescript.player_inventory_select_slot(prev_slot_a)
                                    minescript.player_inventory_select_slot(prev_slot_b)
                            
                            minescript.echo("Your inventory has been scrambled!")  # Notify completion
                        else:
                            minescript.echo("Not enough items in the inventory to scramble!")  # Handle edge cases
                    else:
                        minescript.echo("Failed to retrieve inventory!")  # Handle potential errors
                    time.sleep(15)

    except Exception as e:
        minescript.echo(f"An error occurred: {e}")

# Dictionary to map weather conditions to the corresponding action
weather_conditions = {
    "clear": "/weather clear",
    "rain": "/weather rain",
    "thunder": "/weather thunder"
}

# Function to process the weather command in chat
def weather_command(message, c):
    # Extract the weather condition after '!weather'
    command_parts = message.split()
    if len(command_parts) > 1:  # Ensure there is something after '!weather'
        weather_condition = command_parts[1].lower()

        # Check if the condition is valid (clear, rain, thunder)
        if weather_condition in weather_conditions:
            # Construct the message
            weather_message = f"{c.author.name} made it {weather_condition}"
            # Execute the corresponding weather command
            minescript.execute(weather_conditions[weather_condition])
            minescript.echo(weather_message)
            # Optional delay to prevent rapid command execution
            time.sleep(15)

difficulty_conditions = {
    "peaceful": "/difficulty peaceful",
    "easy": "/difficulty easy",
    "normal": "/difficulty normal",
    "hard": "/difficulty hard"
}

# Function to process the difficulty command in chat
def difficulty_command(message, c):
    # Extract the difficulty condition after '!difficulty'
    command_parts = message.split()
    if len(command_parts) > 1:  # Ensure there is something after '!difficulty'
        difficulty_condition = command_parts[1].lower()

        # Check if the condition is valid (clear, rain, thunder)
        if difficulty_condition in difficulty_conditions:
            # Construct the message
            difficulty_message = f"{c.author.name} made it {difficulty_condition}"
            # Execute the corresponding difficulty command
            minescript.execute(difficulty_conditions[difficulty_condition])
            minescript.echo(difficulty_message)
            # Optional delay to prevent rapid command execution
            time.sleep(15)

gamemode_conditions = {
    "survival": "/gamemode survival",
    "adventure": "/gamemode adventure",
    "creative": "/gamemode creative",
    "spectator": "/gamemode spectator"
}

# Function to process the gamemode command in chat
def gamemode_command(message, c):
    # Extract the gamemode condition after '!gamemode'
    command_parts = message.split()
    if len(command_parts) > 1:  # Ensure there is something after '!gamemode'
        gamemode_condition = command_parts[1].lower()

        # Check if the condition is valid (clear, rain, thunder)
        if gamemode_condition in gamemode_conditions:
            # Construct the message
            gamemode_message = f"{c.author.name} changed the mode to {gamemode_condition}"
            # Execute the corresponding gamemode command
            minescript.execute(gamemode_conditions[gamemode_condition])
            minescript.echo(gamemode_message)
            # Optional delay to prevent rapid command execution
            time.sleep(45)
            minescript.execute('/gamemode survival')
            time.sleep(15)

# List of mobs that cannot be summoned
restricted_mobs = ["wither", "warden", "elder_guardian", "ender_dragon", "tnt", "ghast"]

# Dictionary of special mobs with their corresponding summon commands
special_mobs = {
    "killer_rabbit": "/summon rabbit ~ ~ ~ {RabbitType:99}",
    "toast": "/summon rabbit ~ ~ ~ {CustomName:'{\"text\":\"Toast\"}',CustomNameVisible:1}",
    "jeb_sheep": "/summon sheep ~ ~ ~ {CustomName:'{\"text\":\"jeb_\"}',CustomNameVisible:1}",
    "giant": "/summon giant",
    "zombie_horse": "/summon zombie_horse",
    "illusioner": "/summon illusioner"
}

# Function to process the summon command in chat
def summon_command(message, c):
    # Extract the summon condition after '!summon'
    command_parts = message.split()
    if len(command_parts) > 1:  # Ensure there is something after '!summon'
        summon_condition = command_parts[1].lower()

        # Check if the summon condition is in the restricted list
        if summon_condition in restricted_mobs:
            minescript.echo(f"{c.author.name}, the entity {summon_condition} is not allowed. Please choose a different entity.")
        elif summon_condition in special_mobs:
            # If it's a special mob, use the predefined summon command
            summon_command = special_mobs[summon_condition]
            summon_message = f"{c.author.name} summoned a special {summon_condition}!"
            try:
                # Execute the summon command
                minescript.execute(summon_command)
                minescript.echo(summon_message)
                # Optional delay to prevent rapid command execution
                time.sleep(15)
            except Exception as e:
                # Provide feedback in case of an error
                minescript.echo(f"Failed to summon '{summon_condition}'. Error: {str(e)}")
        else:
            # Default summon behavior for standard mobs
            summon_command = f"/summon minecraft:{summon_condition}"
            summon_message = f"{c.author.name} summoned a {summon_condition}!"
            try:
                # Execute the summon command
                minescript.execute(summon_command)
                minescript.echo(summon_message)
                # Optional delay to prevent rapid command execution
                time.sleep(15)
            except Exception as e:
                # Provide feedback in case of an error
                minescript.echo(f"Failed to summon '{summon_condition}'. Please ensure it's a valid mob name. Error: {str(e)}")

timeset_conditions = {
    "day": "/time set day",
    "noon": "/time set noon",
    "night": "/time set night",
    "midnight": "/time set midnight"
}

# Function to process the timeset command in chat
def timeset_command(message, c):
    # Extract the timeset condition after '!timeset'
    command_parts = message.split()
    if len(command_parts) > 1:  # Ensure there is something after '!timeset'
        timeset_condition = command_parts[1].lower()

        # Check if the input is a predefined time condition
        if timeset_condition in timeset_conditions:
            # Construct the message
            timeset_message = f"{c.author.name} set the time to {timeset_condition}."
            # Execute the corresponding timeset command
            minescript.execute(timeset_conditions[timeset_condition])
            minescript.echo(timeset_message)

        # Check if the input is a custom time (numeric value)
        elif timeset_condition.isdigit():
            custom_time = int(timeset_condition)
            if 0 <= custom_time <= 24000:  # Validate the range
                # Construct and execute the custom time command
                custom_time_command = f"/time set {custom_time}"
                timeset_message = f"{c.author.name} set the time to {custom_time}."
                minescript.execute(custom_time_command)
                minescript.echo(timeset_message)
            else:
                # Handle out-of-range custom times
                minescript.echo(f"{c.author.name}, please enter a valid time between 0 and 24000.")
        else:
            # Handle invalid conditions
            minescript.echo(f"{c.author.name}, unknown time condition: '{timeset_condition}'. Use a valid time or a number between 0 and 24000.")
        time.sleep(15)

# Define movement commands and their corresponding key bindings
movement_conditions = {
    "forward": "key.forward",
    "back": "key.back",
    "left": "key.left",
    "right": "key.right",
    "jump": "key.jump"
}

# Function to process movement commands in chat
def movement_command(message, c):
    # Extract the movement condition after the command
    command_parts = message.split()
    if len(command_parts) > 1:  # Ensure there is something after '!movement'
        movement_condition = command_parts[1].lower()

        # Check if the condition is valid (forward, back, left, right, jump)
        if movement_condition in movement_conditions:
            # Construct the message
            movement_message = f"{c.author.name} made you move {movement_condition}"
            minescript.press_key_bind(movement_conditions[movement_condition], True)
            time.sleep(0.5)
            minescript.press_key_bind(movement_conditions[movement_condition], False)
            minescript.echo(movement_message)
            time.sleep(15)

# Define slot commands and their corresponding key bindings
hotbar_conditions = {
    "1": "key.hotbar.1",
    "2": "key.hotbar.2",
    "3": "key.hotbar.3",
    "4": "key.hotbar.4",
    "5": "key.hotbar.5",
    "6": "key.hotbar.6",
    "7": "key.hotbar.7",
    "8": "key.hotbar.8",
    "9": "key.hotbar.9"
}

# Function to process slot switch commands in chat
def slot_command(message, c):
    # Extract the slot slot number after the command
    command_parts = message.split()
    if len(command_parts) > 1:  # Ensure there is something after '!slot'
        hotbar_slot = command_parts[1]

        # Check if the slot is valid (1 through 9)
        if hotbar_slot in hotbar_conditions:
            hotbar_message = f"{c.author.name} switched to slot {hotbar_slot}"
            minescript.press_key_bind(hotbar_conditions[hotbar_slot], True)
            minescript.echo(hotbar_message)
            time.sleep(15)

def give_command(message, c):
    # Split the message to extract the item details
    command_parts = message.split(maxsplit=1)  # Split into "!give" and the rest of the message
    if len(command_parts) > 1:  # Ensure there is something after "!give"
        item_details = command_parts[1]  # Everything after "!give"

        # Attempt to extract the item and quantity
        parts = item_details.split()  # Split item details into parts (e.g., "minecraft:diamond 10")
        if len(parts) == 2:  # Ensure there are exactly two parts: item and quantity
            item = parts[0]
            try:
                quantity = int(parts[1])  # Parse the quantity as an integer
                if 0 < quantity <= 16:  # Check if the quantity is within the valid range
                    # Construct the /give command
                    give_command = f"/give @p {item} {quantity}"
                    minescript.execute(give_command)

                    # Provide feedback in the chat
                    give_message = f"{c.author.name} gave you {quantity} {item}(s)"
                    minescript.echo(give_message)
                    time.sleep(15)
                else:
                    # Notify if the quantity is out of range
                    error_message = f"{c.author.name}, you can only give between 1 and 16 items."
                    minescript.echo(error_message)
            except ValueError:
                # Notify if the quantity is not a valid number
                error_message = f"{c.author.name}, please specify a valid number for the quantity. Usage: !give <item> <count>"
                minescript.echo(error_message)
        else:
            # Notify if the input format is incorrect
            error_message = f"{c.author.name}, please specify the item and quantity. Usage: !give <item> <count>"
            minescript.echo(error_message)
    else:
        # Notify if the command is incomplete
        error_message = f"{c.author.name}, please specify an item to give. Usage: !give <item> <count>"
        minescript.echo(error_message)

def effect_command(message, c):
    # Split the message to extract the effect and amplifier
    command_parts = message.split()
    if len(command_parts) > 2:  # Ensure there is enough input after "!effect"
        effect = command_parts[1].lower()  # Extract the effect (case-insensitive)

        # Exclude "instant_damage" from being used
        if effect == "instant_damage":
            error_message = f"{c.author.name}, the effect 'instant_damage' is not allowed. Please choose a different effect."
            minescript.echo(error_message)
            return

        try:
            amplifier = int(command_parts[2])  # Extract and validate the amplifier
            if amplifier < 1 or amplifier > 5:  # Ensure amplifier is within the range 1-5
                raise ValueError("Amplifier out of range")
        except ValueError:
            error_message = f"{c.author.name}, please provide a valid amplifier (1-5). Usage: !effect <effect> <amplifier>"
            minescript.echo(error_message)
            return

        # Construct the /effect command
        effect_command = f"/effect give @p {effect} 20 {amplifier} true"
        minescript.execute(effect_command)

        # Notify the player
        effect_message = f"{c.author.name} gave you {effect} {amplifier}."
        minescript.echo(effect_message)
        time.sleep(50)
    else:
        # Notify the user about incomplete command
        error_message = f"{c.author.name}, please specify an effect and amplifier. Usage: !effect <effect> <amplifier>"
        minescript.echo(error_message)

# List of restricted enchantments
restricted_enchants = ["vanishing_curse", "binding_curse"]

# Function to process the enchantment command in chat
def enchant_command(message, c):
    # Split the message to extract the enchantment and level
    command_parts = message.split()
    if len(command_parts) > 2:  # Ensure there is enough input after "!enchant"
        enchantment = command_parts[1].lower()  # Extract the enchantment (case-insensitive)

        # Exclude "vanishing_curse" and "binding_curse" from being used
        if enchantment in restricted_enchants:
            error_message = f"{c.author.name}, the enchantment '{enchantment}' is not allowed. Please choose a different enchantment."
            minescript.echo(error_message)
            return

        try:
            level = int(command_parts[2])  # Extract the level
        except ValueError:
            error_message = f"{c.author.name}, please provide a valid enchantment level. Usage: !enchant <enchantment> <level>"
            minescript.echo(error_message)
            return

        # Construct the /enchant command
        enchant_command = f"/enchant @p {enchantment} {level}"
        minescript.execute(enchant_command)

        # Notify the player
        enchant_message = f"{c.author.name} enchanted your item with {enchantment} {level}."
        minescript.echo(enchant_message)
        time.sleep(15)
    else:
        # Notify the user about incomplete command
        error_message = f"{c.author.name}, please specify an enchantment and level. Usage: !enchant <enchantment> <level>"
        minescript.echo(error_message)


def main():
    video_id = "qGGrQaWRiuM"  # Replace with your YouTube live video ID
    fetch_youtube_chat(video_id)
    minescript.echo("Finished fetching chat.")

if __name__ == "__main__":
    main()
