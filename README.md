# InsertGroupNameRepository
This is the official repository of GitHub from the group "Insert Group Name" 
Euro Exchange Calculator (Bills + Coins)

This project is a Euro change calculator that computes the exact change, optimizes bill/coin usage, and updates a real cash register inventory after each transaction.

It supports all euro denominations and handles monetary values precisely by converting everything to cents.

✨ Features

✔️ Accurate change calculation using cents (no floating-point errors)

✔️ Supports all euro denominations (bills + coins)

✔️ Uses a real cash register stock and only returns available bills/coins

✔️ Automatically updates the cash register inventory

✔️ Warns if exact change cannot be returned

✔️ Displays final inventory and total cash value

✔️ Clean, modular, and well-documented code
__________________________________________________________________________________

📂 Project Structure

The program includes:

- A global dictionary of euro denominations.
- A configurable initial cash register stock.
- A function that computes change using available units.
- A display function that prints the change breakdown.
- A terminal-based execution workflow.
__________________________________________________________________________________

🧮 How It Works

The user inputs:
  
 - Product price.
  
 - Amount paid.

The program:
 - Converts everything to cents.
  
 - Calculates the required change.

 - Determines how many bills/coins can actually be given.
   
 - Updates the inventory in real time
   
It then displays:
   
 - Total change

 - Breakdown of each bill/coin used
   
 - Warning if exact change is impossible
  
 - Final inventory and total cash value
