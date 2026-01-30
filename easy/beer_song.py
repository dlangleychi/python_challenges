class BeerSong:
    STARTING_VERSE = 99
    ENDING_VERSE = 0

    @staticmethod
    def _bottle_phrase(num):
        if num == 0:
            return 'no more bottles'
        if num == 1:
            return '1 bottle'
        return f'{num} bottles'
    
    @staticmethod
    def _pronoun(num):
        if num == 1:
            return 'it'
        return 'one'
    
    @staticmethod
    def verse(num):
        if num == 0:
            return (
                "No more bottles of beer on the wall, "
                "no more bottles of beer.\n"
                "Go to the store and buy some more, "
                "99 bottles of beer on the wall.\n"
                )
        return (
            f"{BeerSong._bottle_phrase(num).capitalize()} of beer on the wall, "
            f"{BeerSong._bottle_phrase(num)} of beer.\n"
            f"Take {BeerSong._pronoun(num)} down and pass it around, "
            f"{BeerSong._bottle_phrase(num - 1)} of beer on the wall.\n"
        )
    
    @staticmethod
    def verses(start, end):
        return '\n'.join(BeerSong.verse(num) 
                         for num in range(start, end - 1, -1))
    
    @staticmethod
    def lyrics():
        return BeerSong.verses(
            BeerSong.STARTING_VERSE, BeerSong.ENDING_VERSE)
    