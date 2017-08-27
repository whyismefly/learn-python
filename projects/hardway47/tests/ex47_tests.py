from nose.tools import *
import ex47.game import Room


def test_room() :
    gold=Room("goldroom",
              """golds in.
              a door north""")
    assert_equal(gold.name,"goldroom")
    assert_equal(gold.paths,[])

def test_room_paths():
    center=Room("center","test room in the center")
    north=Room("North","test room in north")
    south=Room("South","test room in south")

    center.add_paths(['north':north,'south':south])
    assert_equal(center.go("north"),north)
    assert_equal(center.go('south'),south)

def test_map():
    start=Room("start","go west and down a hole")
    west=Room("trees","trees here,go east")
    down=Room("dungeon","dark here,go up")

    start.add_paths(['west': west, 'down': down])
    west.add_paths(['east':start])
    down.add_paths(['up': start])

    assert_equal(start.go('west'),west)
    assert_equal(start.go('west').go('east'),start)
    assert_equal(start.go('down').go('up'),start)