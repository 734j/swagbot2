from cowsay import read_dot_cow, cowthink
from io import StringIO

# Cowfiles for the cowsay command
# https://tldr.inbrowser.app/pages/common/cowsay


##
## Blowfish
##
blowfish = read_dot_cow(StringIO("""
$the_cow = <<EOC;
   $thoughts
    $thoughts
               |    .
           .   |L  /|
       _ . |\\ _| \\--+._/| .
      / ||\\| Y J  )   / |/| ./
     J  |)'( |        ` F`.'/
   -<|  F         __     .-<
     | /       .-'. `.  /-. L___
     J \\      <    \\  | | O\\|.-'
   _J \\  .-    \\/ O | | \\  |F
  '-F  -<_.     \\   .-'  `-' L__
 __J  _   _.     >-'  )._.   |-'
 `-|.'   /_.           \\_|   F
   /.-   .                _.<
  /'    /.'             .'  `\\
   /L  /'   |/      _.-'-\\
  /'J       ___.---'\\|
    |\\  .--' V  | `. `
    |/`. `-.     `._)
       / .-.\\
 VK    \\ (  `\\
        `.\\

EOC
"""))

##
## A small cow, artist unknown
##
small = read_dot_cow(StringIO("""
$eyes = ".." unless ($eyes);
$the_cow = <<EOC;
       $thoughts   ,__,
        $thoughts  ($eyes)____
           (__)    )\\
            $tongue||--|| *
EOC
"""))

##
## A kitten of sorts, I think
##
kitty = read_dot_cow(StringIO("""
$the_cow = <<EOC;
     $thoughts
      $thoughts
       ("`-'  '-/") .___..--' ' "`-._
         ` *_ *  )    `-.   (      ) .`-.__. `)
         (_Y_.) ' ._   )   `._` ;  `` -. .-'
      _.. `--'_..-_/   /--' _ .' ,4
   ( i l ),-''  ( l i),'  ( ( ! .-'    
EOC
"""))

##
## A cow with a bong, from lars@csua.berkeley.edu
##
bong = read_dot_cow(StringIO("""
$the_cow = <<EOC;
         $thoughts
          $thoughts
            ^__^ 
    _______/($eyes)
/\\/(       /(__)
   | W----|| |~|
   ||     || |~|  ~~
             |~|  ~
             |_| o
             |#|/
            _+#+_
EOC
"""))

##
## A cow being milked, probably from Lars Smith (lars@csua.berkeley.edu)
##
supermilker = read_dot_cow(StringIO("""
$the_cow = <<EOC;
  $thoughts   ^__^
   $thoughts  ($eyes)\\_______        ________
      (__)\\       )\\/\\    |Super |
       $tongue ||----W |       |Milker|
          ||    UDDDDDDDDD|______|
EOC
"""))



