# Command Line Tarot

This project is meant to be a ~~nerdy~~ convenient way to get a tarot reading via the command line interface!

```ascii
MMMMMMMMMMMMMN0xo:;,,,,.  .',,,;:lx0NWMMMMMMMMMMMM
MMMMMMMMMWXxc,,;cdk0KXk'  .xXX0kdl;,,cxKWMMMMMMMMM
MMMMMMMNkc',lkKWMMMMMNc....;XMMMMMWXkl,':kNMMMMMMM
MMMMMNk;':kNMMMMMMMMWx.;O0c.oWMMMMMMMMNOc',xNMMMMM
MMMW0:.:OWMMMMMMMMMM0,.kWM0''OMMMMMMMMMMW0c.;OWMMM
MMNx.'kNMMMMMMMMMMMNl.lNMMWd.:XMMMMMMMMMMMWO,.oNMM
MNo.;0MMMMMMMMMMMMWx.,KMMMMX:.dWMMMMMMMMMMMMKc.lXM
Wd.;0WWWWWWWWWWWWW0,.xNWWWWWk.'OWWWWWWWWWWWWWK:.lN
k. .,;;;;;;;;;;;;;. .,;;;;;;;. .;;;;;;;;;;;;;,. .x
:.;:. .lxkkkOkkOkc.'dOkkOOOkOx, ;kOkkOkkkkl' .;:.,
.'0WKd;';dKWMMMMK;.xWMMMMMMMMMO.'0MMMMWXx:';o0WK;.
.:XMMMN0o,':xXWWo.cNMMMMMMMMMMWo.cNMNkc',lONMMMNc
 :NMMMMMMNOc,,cl.'0MMMMMMMMMMMMK;.cl,'ckXMMMMMMWl
.;XMMMMMMMMWXx;  ,OWMMMMMMMMMMW0;  ,xKWMMMMMMMMN:
'.OMMMMMMMMMMWo.';';dKWMMMMWXx:','.cNMMMMMMMMMM0'.
o.cNMMMMMMMMMO''ON0o,':x0Kkc',lONK,.xWMMMMMMMMWo.c
K;.xWMMMMMMMX:.dWMMMNx' .. .dXWMMWk.,KMMMMMMMWk.'0
MO'.kWMMMMMWd.:XMMW0o;':lo:',o0WMMNl.lNMMMMMWO'.kW
MWO,.dNMMMMO''OWKx:';o0WMMWKd;';dKW0,.kWMMMWx''kWM
MMMKc.:0WMX:.cxc',lONMMMMMMMMW0o,':xl.;KMWKc.;0WMM
MMMMNk,.cOo. .'ckXMMMMMMMMMMMMMMNOc,.  lOo''dNMMMM
MMMMMMXx;.. 'dXWMMMMMMMMMMMMMMMMMMWXx,  .,dXMMMMMM
MMMMMMMMNOl,':oOXWMMMMMMMMMMMMMMWXOd:''ckNMMMMMMMM
MMMMMMMMMMMNOo:;,;:lodxkkkkxdol:;,,:oOXWMMMMMMMMMM
MMMMMMMMMMMMMMWXOo:'..      ..';okXWMMMMMMMMMMMMMM
```

---

## Instructions

> **Note:** Python 3 is required.

Clone this repository and `cd` into the `/command_line_tarot` directory. To ensure that the CLI Tarot is working properly, invoke the help text:

```bash
$ python3 main.py --help

usage: main.py [-h] [-fd [FREE_DRAW] | -s | -cm [CARD_MEANING] | -cd [CARD_DIRECTORY]] [{None}]

A command line tarot reader!

positional arguments:
  {None}                Pass in no args for a single card reading

optional arguments:
  -h, --help            show this help message and exit
  -fd [FREE_DRAW], --free_draw [FREE_DRAW]

                            'Free Draw'

                            Read a specific number of cards
                            (passed as an integer after the '-fd'
                            flag; defaults to a single-card pull)

  -s, --seen
                            'Seen Heard Held'

                            A 4-card spread which reveals:
                            Card 1 - What needs to be seen
                            Card 2 - What needs to be heard
                            Card 3 - What needs to be held
                            Card 4 - Action to be taken

                            Optional: Pull a single card afterwards as a clarifier

  -cm [CARD_MEANING], --card_meaning [CARD_MEANING]
                        Display the meaning of a specified card
  -cd [CARD_DIRECTORY], --card-directory [CARD_DIRECTORY]
                        Display the meaning of a specified card
```

---

## Basic Commands

- Command 1
- Spread 2
- Etc etc
