# Python telegram bot trainer

Your ultimate python telegram trainer bot

## Demo bot

https://t.me/coolpythonbot

## Getting Started

1. Create a Github account
2. Fork this repo
3. Open your repo on gitpod  `https://gitpod.io/#<url of your repo>`

## How to run code?

1. `source venv/bin/activate`
2. `pip3 install -r requirements.txt`
3. Change your token value here `updater = Updater("1646131932:AAHLYwh0qaE0T3Rk_hakznz75SCPs5Ds02s")`
4. `python3 main.py`

## Example projects

https://github.com/python-telegram-bot/python-telegram-bot/wiki/Examples



Paper x Scissors
P       S
 
             |  P  (p1)  | S (p1)
  -          |  -        | - 
  P (p2)     | Draw      | p1
  S (p2)     | p2        | Draw


  instruction


handler -> ic of deciding who wins the game

# State (Memory) -- global
player1 = "scissors"
player2 = "paper"

# Step1: Issue commands
/scissors
-> player1 = "scissors"
/paper
-> player2 = "paper"

# Step 2: Ready to evaluate

             |  P  (p1)  | S (p1)
  -          |  -        | - 
  P (p2)     | Draw      | p1
  S (p2)     | p2        | Draw

  3 if-else

  Lookup the table (with somekind of logic)

  -> Return result
  send_message(result)


## Add in the stone (Evalute result)

Legend
- P: Paper 
- Sc: Scissors
- St: Stone


             |  P  (p1)  | Sc (p1) | St(p1)
  -          |  -        | -       |   - 
  P (p2)     | Draw      | p1      |  p2
  Sc (p2)    | p2        | Draw    |  p1
  St(p2)     |  p1       |  p2     | Draw



7 if-else statement


        
arr = [     0 P    1 Sc   2 St
Paper 0    [ Draw, p1, p2],
Sc    1    [ p2, Draw, p1],
St    2    [ p1, p2, Draw],
]

paper -> 0
scissors -> 1
stone -> 2

p2 : scissor 1
p1 : stone 2


arr[p2][p1]
arr[1][2] = p1 wins

p2: paper 0
p1: stone  2
arr[0][2] = p2 wins

2 parts

1. issue commands - parse commands and store state ✅
    - 

/scissors
/stone
/paper

player1 = 'paper'
player2 = 'stone'

evaluate




2. evaluate result ✅
    - gonna use the matrix method to evaluate




arr[0] = [Draw, p1, p2]
arr[0][0] = Draw

row = p2
col = p1

