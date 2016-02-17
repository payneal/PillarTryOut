// http://www.slideshare.net/amritayan/test-driven-development-in-c

#include <assert.h> 
#include <stdio.h>
#include <stdlib.h>

#include "bowling_game.h"


static void test_gutter_game(){
    bowling_game_init(); 
    for (int i=0; i<20; i++ ){
        bowling_game_roll(0); 
        assert( bowling_games_score() == 0 && 
                  "test_gutter_game()"); 
    }
}

int main() {
    test_gutter_game(); 
}

