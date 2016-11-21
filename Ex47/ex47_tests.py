from nose.tools import*
from ex47.game import Room

def test_room():
    gold = Room("GoldRoom"
                 """This room has gold in it you can grab.
                 There's a door to the north.""")
    asser_equal(gold.name, "GoldRoom")
    asser_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "test toom in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("south", "Test room in the south.")

    center.add_paths({'north':north, 'south':south})

    assert_equal(cemter.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are trees here, you can go east.")
    down = Room("Dungeons", "It's dark down here, you can go up.")

    start.add_paths({'west':west , 'down': down})
    west.add_paths({'east':start})
    down.add_path({'up', start})

    assert_equal(start.go('west'),west)
    assert_equal(start.go('west').go('east'),start)
    assert_equal(start.go('down').gp('up'), start)
    