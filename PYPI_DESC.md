# Command Line Tarot

This project is meant to be a ~~nerdy~~ convenient way to get a tarot reading via the command line interface!

---

# 🚧 This Package is Under Construction 🚧

This is a beta/test version `0.1.3` of the Command Line Tarot CLI tool!

Currently missing most card interpretations. However, the ASCII art is fully accessible and complete.

---

## Instructions for Installing from PyPI

Create and activate a virtual environment or a `conda` env that has Python 3.9, then run the following:

```
$ pip install cli-tarot
```

To ensure that the package is properly installed, run:

```
$ cli-tarot --help
```

---

## Basic Commands

### Single Card Readings

To do a basic single-card reading, type in the following command:

`$ cli-tarot`

Sample output from the above:

```bash
✨ Your single card drawing is: ✨

    (26) Five of Wands
```

### Querying the Meanings (and/or Artwork) of Specific Cards Via Index Number

If you forgot to pass in the `-i` / `--interpretation` flag even though you wanted to know the meaning of the card, that's ok; that's what the `-cm` / `--card_meaning` flag is for! The number listed before the card name (in the case of the example above, `26`) is the index number for the card; pass that in after invoking the Card Meaning functionality, like the command below:

`$ cli-tarot -cm 26`

```bash
...looking up meaning for:

    (26) Five of Wands


    How to interpret the Five of Wands:

    [ meaning ]
```

If you'd also like to see the ASCII art for a specific card along with its meaning, add the `-a` flag like so:

`$ cli-tarot -cm 26 -a`

```
Displaying card art for:

    (26) Five of Wands

    lodooodddoodddddddddddddddoooooddddddddddddddddddddddddddddddoooooddddddddddxddddxdddddddo
    lkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkdloxkxooxkkkOkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx
    lkkkkkkkkkookkkkkkkkkkkkkkkkkkkkkkkkkkkkkxl;lko:lxkkkOkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx
    lxkkkkkkkxc;lddkkkkkkkkkkkkkkkkkkkkkkkkkkkko:,;lxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx
    lkkkkkkkdc:;,:okkkkkkkkkkkkkkkkkkkkkkkkkkkkkdoodkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx
    lxkkkkkkxolc;,cxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx
    lxkkkkkkkkl;;,;lxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxdxxkkkkkkkkkkx
    lxkkkkkkkkd:,;,:xkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxl,,cxkkkkkkkkkx
    lxkkkkkkddko;:;;okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxc,',cxkkxxkkkkx
    lkkkkkkxdcld:,;;okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkddxkkkxl;;;;lxkxkkkkkx
    lkkkkkkkdc,;;,:;cxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxo:;ldxkkxc;:;:dkxkkkkkd
    lkkkkkkkxoc:c,,,;xkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxc,';oxkkko::;,okxxkkkkd
    lkkkkkkkkkddd;,,'lkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxl::;cxkkkkd::;,lkxxkkkkd
    lkkkkkkkkkkkxc,,.:kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxl:;,:oxkkkkxc::,:llxkxkkd
    lkkkkkkkkkkkxl;,'ckkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkd:;,cxkkkkkkxl::,,;;oxxkkd
    lkkkkkkkkkkkkl;;,;ddoxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkdcodc;,:dkkkkkkkkl;:;;lddxkkkd
    lkkkkkkkkkkkko;,'.;;;lxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxo:':c;,;okkkkkkkddo:;;,lkxxkkkd
    lkkkkkkkkkkkkx:,,..cddxkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkdcc:;;,lkkkkkkkxc,,,;,,cxkxdxkd
    lkkkkkkkkkkkkkl,,.'okkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkx:;,cxkkkkkkkxdc;,;,'cxdc:cxd
    lkkkkkkkkkkkkko;,',dkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxl;,;dkkkkkkkkkkkxl;;,;::;,;dd
    lkkkkkkkkkkkkkkl;,'lkkkOkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkko;',lkkkkkkkkkkkkko;;,',;,;okd
    lkkkkkkkkkkkkkkd:,':xkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkd:'';:cxkkkkkkkxxdol:;,'';lxkko
    okkkkkkkkkkkkkkkc,,,oOkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkdc,',::cdkkkkxxolc:;,,;,.,oxxkko
    dkkkkkkkkkkkkkkko;,,lkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxl;,;oxodxdolc::;;,',,',,.;dkxxko
    okkkkkkkkkkkkkkkx;,';xkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkko;,,cl;,;c:;;,,,,,,'';:;,':dkxxko
    okkkkkkkkkkkkkkkkc,''lkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkxkxxo:,',:;,,,,;:clc:;,,;lxxc,;;okxxko
    okkkkkkkkkkkkkkkko,,';xkkkkkkkkkkkkkkkkkkkkkkxxxxxxxdlc:,,,'',,;:codol:;,,;lxxxxl;;;oxxxko
    okkkkkkkkkkkkkkkkd;''.cxkkkkkkkkkkkkxolcloxdoodolcc:;,'''.';codxkxol::,,;ldkxxxxo:;:lxxxko
    okkkkkkkxkkkkkkkkkc',',lkkkxkkkkkxdl:c:,',;;cdxl,,,,;:;'''cxkkkxdc;;;';ldxxkkoc:c:;;lxxxko
    dkkkkkkkxkkkkkkkkxlcl;,lkxxxxdoxkxc;cllc,..'cdo;,coddc,'.'lxxxdc:,'':ldkkxxkkxdlc:,,:dxxko
    dkkkkkkkkkkkkkkkkkoldc'ckxxxo:,:lc;;:cdxo;.,dOd;cxkxo:,,'';odl;''',:oxxxxxxkkkkkxl,;:oxxko
    dkkkkxkkkkkxkkkkkxl;;,':xdolc;',,,,',;;co;.:k0o,lxxo;,'';l:;;,'.';::;:oxxxxxkkkxkd:;;:oxko
    xkkkxxoloxxxkxxkxloo,,''::,,,;:c;'';:'.:c''d00x;',::,''.:l;'.''',col:',cxkxxkkkkxo:,;;:dko
    xkxdc,...cdxkxxxolkx,,;'''...,;,,',;'...;:lO000l..',,'.,,'.':dl;::cxo;,;lkkkkxxkxlldl,;od:
    dxl'...',;coolc::x0d,',',;..col:;'.'....:c;cddl,....''',..:dkkdl:::oc'.,:c::lddddccd:.,cc;
    xx:'..'',oo::,,lkOx:;,'.,l;,odoc,',...................';;';ll;;:''cdo,..',...;::;;lc,'';:;
    dxl;'..'cdl:::d0Kd;lxl,'..';::::;::,.........''''','..'cd:,;c:,,'.,clc;,;:,.',;:,lOl'',,,'
    xkxoc,':oc,;ok0KKdcdkl,'.,;;;:;;::cc:;,''',,'.',;,'.,:;:doodo:'.....';;:c:'.....,xk;',,';;
    dkkkd::ldocxK0KKklokko,.';::cc:;,;;;;,,;:::,.',,....,:lclc;:,.........'::;'.','':xo.';,,ol
    dkkdclxxxdld000O:;dkkd,..,,,:cccccc,.',,,,'',;'....'';odolcc::c;......':c:'.;odxkx;',;;,ll
    dkxlloodxxoloxxo:'ckkxc,'...';;;;,,,;'.............'..:xxxkkkocc,,;;,',:ccc''d00x::c;;,'cl
    xxodkl':dxxxdlll:';dkkd:,'..',;:::::c:'.''...''...'''.,dkxdoollllodol:ldddd;.,lc,:xd;',':c
    xoxOOl..:dxxxxxxdc,lkkxc,'.,;,,:ccc:;;;,....','...,,,''col:cddxkxxkkdxkxdxxl;,',lxxx:.'.:c
    dlxOo,....:dxxxxkxclkkko,,';o:.,:c:;,'............,:c:,;cxd:dOkddxkkxodxdxdc;''lxxxxl,'';:
    koclc,,::..;oxxxxl,,dkkdc:::oo,,:::;...,'.','......:o::xO0o;cxkxxkxdocokdl:;,.'lxxxko;,',;
    kkdllodkkc..cxoc,,,;:okkxxxxl,,;;;,'',;c;..''...'''::ok0Od:,cxkdxkkxoldd:,;,''.;dxxkd:,'',
    kkkkkkkdc,',,,'..;;;;;cdxxko;,;,..,;,;:c:,..,::;:cll:cllc;,,lkkxxkxllxd;,;;,;,''cdxkxc,,',
    kkkkkxc'.',,.....;,',;:;lxoc;,'.';:;;;:cc;..:oxoldkxl:collc:odxkkdcloc,;cc;,,,'.,cdkkl,'.'
    kkkkxc'.,:;',;,.',.,,.,,,::;'.,;c:''',:cc:,.,cddcoxxllxkkxclkkxxdcld:,:llc;;;,..;,cxko,...
    kkkd:;:;;,,,:oo,::.,;''.';,,,:ccc;''',clc:,,lxkdlokdlokkko;clllddlc,.;llc;:c;'..,,lxkd;'.'
    kko;::;,,,;:lc,.;l:;;;;'',',:ccc:',,'',:cloclxkxccxlcxkxlcoo:;,;c:,..,;cc;;:;..',cdxkxc'.'
    kkxoooc;;;;:;;coxkkkoc;;;;,'looo:;lo;'';oxxocodoclo:cxd:;lddol:;,;,,,,,:ccc:;;:;;dkkkxl,,'
    kkkkkkl,;::;:dkkkkkkkxl;,;'cxkkdcokl;,..;dkdc:cclxdclo,'lxxxxol:;::;;:clxkxl;;:;;dkkkkdlc;
    kkkkkkc,;:;;okkkkkkkkkkl,,:dkkdlokd;,,..'cxxl::;;c::ol;codxkdolcldlc:;cclxkd:;:;;okxkkkkxc
    kkkkkd,';:;lxkkkkkkkkkko,,lxkocdkd:,,';;'cxko:;;;'.ld;:olcoddxo:;,::c;;:cdkkl;,;;:xkxkkkx:
    kkkkd:,;;,:xOkkkkkkkkkkocoddl,ckkl,,',o:'cxkdc;,;'cko;coolol:c:;,';::c,;oxkkd:,;:;lxkkkkxc
    kkko:;:;,cxkkkkkkkkkkkllxkx:,,:xkxollddc;:dkxo:,;;xdclxxxxdc;;;,,',coxl:dkkkko;;:;cxkkkkxc
    kxl;::;;lkkkkkkdc;:ldl:dkkl,,;;okkxkkdccc,;cll;';cl:lxxxdl,';:;,cl;oxxo:ldcccol;;;:dkxxxxl
    ko,,;,;oxxxdolc,',;::,;xko,..:c:::::c;;;'...:l:';:,cxxxo:,',::,,;;',oxd:,;,,,,,',;,;::cc:;
    dccc,';cc:;,,'',;;,;;''cl,,,':o:,;::::;;,,,'cxl',,;dxdc;;'';:;,'..'',:oo;,;;;;,,,;,,;;;;,'
    ';do;,,;;;:llccc::::;.';',::,;xkocloool:;::,lxxl;,lxx:,:c;,;;,;::::c;,lxo;;llc::,,;,:llc:,
    ;cdc;:coddddddddolc:,.:c;;;;,;loolcc:lolc:;,cllc:cdxd:,,'',;',;;::::;,cdxl;clclc;,:ldxdlc;
    :od:::;:c::coooodddo;,cl::;::cllllcc;;cc:;::c::,;oxdc,,,..,,',;;;;;;;;,cxd:,::c:;;;;;clc:;
    :cllllol:,,';c::cc:;,,:ccc:::looddolc::;,,;;,,,;oxd:,';:::;,';cccc::::;,cdc,;;:::::;:;;;:;
    :;codddl::c:cllc::;;,'',,,:;,,;;::;:;;::;;;;,,,cdl,,,;ldl;'';::cc:::::c:;ll;:cllllcc::::;,
    ,,,,::::cc;;;::c::;;,,,;;clc:ccllccl:;::::cc;,cdl;,,,;,,,,,;;;;:::;;;;::,:c,;:ccccccc::::,
    :cc:::::::::;;;;:::cc;:cccccccccccloooooccc;;coo;collllllllllolcll:cc;;:;',;,,;colllllll:,
    cccccccllllllllooodddoooooddddoc,,:lolc::::,,;:;,cxxxxxxxxxxxxxxxxdxdl:c:'';,'',;lllooodo:
    ;;;;;:::::ccc::coooddodollooccc::::::;,:c:;,;;;;:clllloxxxxxxxddooddddddoccllcccllc::::cc;
    cc::;;:::ccclc::cclllllllloddolllc:;;;:cloooooooooool:;:cccloddooooooooolooooololcccc::c:;
    llllllllllloooooododdddxxxxxxxxxdddoooollloooooooodoollodllololcccldoc:odooooolllllcccclc;
    olllllllloooooooooooddddxxxxxkkkkkxxxddooloooddoodddoddxxxxxxxxxxddxdolodooooollcc;,,;clc;
    ddoollooddooddddddddddddxxxxkkkkkkkkxxxxddddddooodddddoddddddddddddddddoooollllc;,'.,;:cc;
    dddddddxxxdddddddooooddddxxkkkxkkxxxxxxxxxxxxxxdddddddoooooooooooooooddxddoooll:,,'';;;:;,
    dddddxxxdddoooooooooooddddxxxxkkkkkxxkxxxxxxxxxxxxxxdddddoooooooooooddxxxxxddocclc,,:ccc:;
    ddddddddddoooooooooooooooodddxxxxxdddddoddddxxxxxxxdddxxdddddddddddxxxxxxxxxxxxxxd::odddl:
    dddddddddddddddddddddddxxxxdddddoooooooooodooodddddddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxlcdxdxo:
    ddddddddddddddddddxxxxxxddoooooooooollooloolloooooooodddddddddddddxxxxxxxxxxxxxxxxddxxdxo:
    ::::::::::::::cccccccc:c:::::;;;;;::;;;:;:::ccccc::cccccccc:::cc:cccccccccllllllllllcccc:;



...looking up meaning for:

    (26) Five of Wands


    How to interpret the Five of Wands:

    [ meaning ]
```

### Output Readings to a File

In order to output/save any particular readings, invoke the `-o`/`--output` flag. Certain features such as "card meaning" do not have file output as an option, but this is a useful option for longer free-draw readings and multi-card readings such as the Celtic Cross.

When using the `-o` / `--output` option, there will be a new file created and saved into the current working directory. The name of the file will consist of the reading type + datetime (e.g., `Seen_Heard_Held_Interpreted_20220319-123727.txt`, `Free_Draw_Art_and_Interpretation_20220319-123929.txt`).
