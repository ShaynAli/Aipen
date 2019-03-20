# # # import pygame
# # #
# # # BLACK = (0, 0, 0)
# # # WHITE = (255, 255, 255)
# # # BLUE = (0, 0, 255)
# # # GREEN = (0, 255, 0)
# # # RED = (255, 0, 0)
# # # PURPLE = (255, 0, 255)
# # #
# # #
# # # class Wall(pygame.sprite.Sprite):
# # #     """This class represents the bar at the bottom that the player controls """
# # #
# # #     def __init__(self, x, y, width, height, color):
# # #         """ Constructor function """
# # #
# # #         # Call the parent's constructor
# # #         super().__init__()
# # #
# # #         # Make a BLUE wall, of the size specified in the parameters
# # #         self.image = pygame.Surface([width, height])
# # #         self.image.fill(color)
# # #
# # #         # Make our top-left corner the passed-in location.
# # #         self.rect = self.image.get_rect()
# # #         self.rect.y = y
# # #         self.rect.x = x
# # #
# # #
# # # class Player(pygame.sprite.Sprite):
# # #     """ This class represents the bar at the bottom that the
# # #     player controls """
# # #
# # #     # Set speed vector
# # #     change_x = 0
# # #     change_y = 0
# # #
# # #     def __init__(self, x, y):
# # #         """ Constructor function """
# # #
# # #         # Call the parent's constructor
# # #         super().__init__()
# # #
# # #         # Set height, width
# # #         self.image = pygame.Surface([15, 15])
# # #         self.image.fill(WHITE)
# # #
# # #         # Make our top-left corner the passed-in location.
# # #         self.rect = self.image.get_rect()
# # #         self.rect.y = y
# # #         self.rect.x = x
# # #
# # #     def changespeed(self, x, y):
# # #         """ Change the speed of the player. Called with a keypress. """
# # #         self.change_x += x
# # #         self.change_y += y
# # #
# # #     def move(self, walls):
# # #         """ Find a new position for the player """
# # #
# # #         # Move left/right
# # #         self.rect.x += self.change_x
# # #
# # #         # Did this update cause us to hit a wall?
# # #         block_hit_list = pygame.sprite.spritecollide(self, walls, False)
# # #         for block in block_hit_list:
# # #             # If we are moving right, set our right side to the left side of
# # #             # the item we hit
# # #             if self.change_x > 0:
# # #                 self.rect.right = block.rect.left
# # #             else:
# # #                 # Otherwise if we are moving left, do the opposite.
# # #                 self.rect.left = block.rect.right
# # #
# # #         # Move up/down
# # #         self.rect.y += self.change_y
# # #
# # #         # Check and see if we hit anything
# # #         block_hit_list = pygame.sprite.spritecollide(self, walls, False)
# # #         for block in block_hit_list:
# # #
# # #             # Reset our position based on the top/bottom of the object.
# # #             if self.change_y > 0:
# # #                 self.rect.bottom = block.rect.top
# # #             else:
# # #                 self.rect.top = block.rect.bottom
# # #
# # #
# # # class Room(object):
# # #     """ Base class for all rooms. """
# # #
# # #     # Each room has a list of walls, and of enemy sprites.
# # #     wall_list = None
# # #     enemy_sprites = None
# # #
# # #     def __init__(self):
# # #         """ Constructor, create our lists. """
# # #         self.wall_list = pygame.sprite.Group()
# # #         self.enemy_sprites = pygame.sprite.Group()
# # #
# # #
# # # class Room1(Room):
# # #     """This creates all the walls in room 1"""
# # #
# # #     def __init__(self):
# # #         super().__init__()
# # #         # Make the walls. (x_pos, y_pos, width, height)
# # #
# # #         # This is a list of walls. Each is in the form [x, y, width, height]
# # #         walls = [[0, 0, 20, 250, WHITE],
# # #                  [0, 350, 20, 250, WHITE],
# # #                  [780, 0, 20, 250, WHITE],
# # #                  [780, 350, 20, 250, WHITE],
# # #                  [20, 0, 760, 20, WHITE],
# # #                  [20, 580, 760, 20, WHITE],
# # #                  [390, 50, 20, 500, BLUE]
# # #                  ]
# # #
# # #         # Loop through the list. Create the wall, add it to the list
# # #         for item in walls:
# # #             wall = Wall(item[0], item[1], item[2], item[3], item[4])
# # #             self.wall_list.add(wall)
# # #
# # #
# # # class Room2(Room):
# # #     """This creates all the walls in room 2"""
# # #
# # #     def __init__(self):
# # #         super().__init__()
# # #
# # #         walls = [[0, 0, 20, 250, RED],
# # #                  [0, 350, 20, 250, RED],
# # #                  [780, 0, 20, 250, RED],
# # #                  [780, 350, 20, 250, RED],
# # #                  [20, 0, 760, 20, RED],
# # #                  [20, 580, 760, 20, RED],
# # #                  [190, 50, 20, 500, GREEN],
# # #                  [590, 50, 20, 500, GREEN]
# # #                  ]
# # #
# # #         for item in walls:
# # #             wall = Wall(item[0], item[1], item[2], item[3], item[4])
# # #             self.wall_list.add(wall)
# # #
# # #
# # # class Room3(Room):
# # #     """This creates all the walls in room 3"""
# # #
# # #     def __init__(self):
# # #         super().__init__()
# # #
# # #         walls = [[0, 0, 20, 250, PURPLE],
# # #                  [0, 350, 20, 250, PURPLE],
# # #                  [780, 0, 20, 250, PURPLE],
# # #                  [780, 350, 20, 250, PURPLE],
# # #                  [20, 0, 760, 20, PURPLE],
# # #                  [20, 580, 760, 20, PURPLE]
# # #                  ]
# # #
# # #         for item in walls:
# # #             wall = Wall(item[0], item[1], item[2], item[3], item[4])
# # #             self.wall_list.add(wall)
# # #
# # #         for x in range(100, 800, 100):
# # #             for y in range(50, 451, 300):
# # #                 wall = Wall(x, y, 20, 200, RED)
# # #                 self.wall_list.add(wall)
# # #
# # #         for x in range(150, 700, 100):
# # #             wall = Wall(x, 200, 20, 200, WHITE)
# # #             self.wall_list.add(wall)
# # #
# # #
# # # def main():
# # #     """ Main Program """
# # #
# # #     # Call this function so the Pygame library can initialize itself
# # #     pygame.init()
# # #
# # #     # Create an 800x600 sized screen
# # #     screen = pygame.display.set_mode([800, 600])
# # #
# # #     # Set the title of the window
# # #     pygame.display.set_caption('Maze Runner')
# # #
# # #     # Create the player paddle object
# # #     player = Player(50, 50)
# # #     movingsprites = pygame.sprite.Group()
# # #     movingsprites.add(player)
# # #
# # #     rooms = []
# # #
# # #     room = Room1()
# # #     rooms.append(room)
# # #
# # #     room = Room2()
# # #     rooms.append(room)
# # #
# # #     room = Room3()
# # #     rooms.append(room)
# # #
# # #     current_room_no = 0
# # #     current_room = rooms[current_room_no]
# # #
# # #     clock = pygame.time.Clock()
# # #
# # #     done = False
# # #
# # #     while not done:
# # #
# # #         # --- Event Processing ---
# # #
# # #         for event in pygame.event.get():
# # #             if event.type == pygame.QUIT:
# # #                 done = True
# # #
# # #             if event.type == pygame.KEYDOWN:
# # #                 if event.key == pygame.K_LEFT:
# # #                     player.changespeed(-5, 0)
# # #                 if event.key == pygame.K_RIGHT:
# # #                     player.changespeed(5, 0)
# # #                 if event.key == pygame.K_UP:
# # #                     player.changespeed(0, -5)
# # #                 if event.key == pygame.K_DOWN:
# # #                     player.changespeed(0, 5)
# # #
# # #             if event.type == pygame.KEYUP:
# # #                 if event.key == pygame.K_LEFT:
# # #                     player.changespeed(5, 0)
# # #                 if event.key == pygame.K_RIGHT:
# # #                     player.changespeed(-5, 0)
# # #                 if event.key == pygame.K_UP:
# # #                     player.changespeed(0, 5)
# # #                 if event.key == pygame.K_DOWN:
# # #                     player.changespeed(0, -5)
# # #
# # #         # --- Game Logic ---
# # #
# # #         player.move(current_room.wall_list)
# # #
# # #         if player.rect.x < -15:
# # #             if current_room_no == 0:
# # #                 current_room_no = 2
# # #                 current_room = rooms[current_room_no]
# # #                 player.rect.x = 790
# # #             elif current_room_no == 2:
# # #                 current_room_no = 1
# # #                 current_room = rooms[current_room_no]
# # #                 player.rect.x = 790
# # #             else:
# # #                 current_room_no = 0
# # #                 current_room = rooms[current_room_no]
# # #                 player.rect.x = 790
# # #
# # #         if player.rect.x > 801:
# # #             if current_room_no == 0:
# # #                 current_room_no = 1
# # #                 current_room = rooms[current_room_no]
# # #                 player.rect.x = 0
# # #             elif current_room_no == 1:
# # #                 current_room_no = 2
# # #                 current_room = rooms[current_room_no]
# # #                 player.rect.x = 0
# # #             else:
# # #                 current_room_no = 0
# # #                 current_room = rooms[current_room_no]
# # #                 player.rect.x = 0
# # #
# # #         # --- Drawing ---
# # #         screen.fill(BLACK)
# # #
# # #         movingsprites.draw(screen)
# # #         current_room.wall_list.draw(screen)
# # #
# # #         pygame.display.flip()
# # #
# # #         clock.tick(60)
# # #
# # #     pygame.quit()
# # #
# # #
# # # if __name__ == "__main__":
# # #     main()
# # import pygame
# # from pygame.locals import *
# #
# # # declare our global variables for the game
# # XO = "X"  # track whose turn it is; X goes first
# # grid = [[None, None, None], \
# #         [None, None, None], \
# #         [None, None, None]]
# #
# # winner = None
# #
# #
# # # declare our support functions
# #
# # def initBoard(ttt):
# #     # initialize the board and return it as a variable
# #     # ---------------------------------------------------------------
# #     # ttt : a properly initialized pyGame display variable
# #
# #     # set up the background surface
# #     background = pygame.Surface(ttt.get_size())
# #     background = background.convert()
# #     background.fill((250, 250, 250))
# #
# #     # draw the grid lines
# #     # vertical lines...
# #     pygame.draw.line(background, (0, 0, 0), (100, 0), (100, 300), 2)
# #     pygame.draw.line(background, (0, 0, 0), (200, 0), (200, 300), 2)
# #
# #     # horizontal lines...
# #     pygame.draw.line(background, (0, 0, 0), (0, 100), (300, 100), 2)
# #     pygame.draw.line(background, (0, 0, 0), (0, 200), (300, 200), 2)
# #
# #     # return the board
# #     return background
# #
# #
# # def drawStatus(board):
# #     # draw the status (i.e., player turn, etc) at the bottom of the board
# #     # ---------------------------------------------------------------
# #     # board : the initialized game board surface where the status will
# #     #         be drawn
# #
# #     # gain access to global variables
# #     global XO, winner
# #
# #     # determine the status message
# #     if (winner is None):
# #         message = XO + "'s turn"
# #     else:
# #         message = winner + " won!"
# #
# #     # render the status message
# #     font = pygame.font.Font(None, 24)
# #     text = font.render(message, 1, (10, 10, 10))
# #
# #     # copy the rendered message onto the board
# #     board.fill((250, 250, 250), (0, 300, 300, 25))
# #     board.blit(text, (10, 300))
# #
# #
# # def showBoard(ttt, board):
# #     # redraw the game board on the display
# #     # ---------------------------------------------------------------
# #     # ttt   : the initialized pyGame display
# #     # board : the game board surface
# #
# #     drawStatus(board)
# #     ttt.blit(board, (0, 0))
# #     pygame.display.flip()
# #
# #
# # def boardPos(mouseX, mouseY):
# #     # given a set of coordinates from the mouse, determine which board space
# #     # (row, column) the user clicked in.
# #     # ---------------------------------------------------------------
# #     # mouseX : the X coordinate the user clicked
# #     # mouseY : the Y coordinate the user clicked
# #
# #     # determine the row the user clicked
# #     if (mouseY < 100):
# #         row = 0
# #     elif (mouseY < 200):
# #         row = 1
# #     else:
# #         row = 2
# #
# #     # determine the column the user clicked
# #     if (mouseX < 100):
# #         col = 0
# #     elif (mouseX < 200):
# #         col = 1
# #     else:
# #         col = 2
# #
# #     # return the tuple containg the row & column
# #     return (row, col)
# #
# #
# # def drawMove(board, boardRow, boardCol, Piece):
# #     # draw an X or O (Piece) on the board in boardRow, boardCol
# #     # ---------------------------------------------------------------
# #     # board     : the game board surface
# #     # boardRow,
# #     # boardCol  : the Row & Col in which to draw the piece (0 based)
# #     # Piece     : X or O
# #
# #     # determine the center of the square
# #     centerX = ((boardCol) * 100) + 50
# #     centerY = ((boardRow) * 100) + 50
# #
# #     # draw the appropriate piece
# #     if (Piece == 'O'):
# #         pygame.draw.circle(board, (0, 0, 0), (centerX, centerY), 44, 2)
# #     else:
# #         pygame.draw.line(board, (0, 0, 0), (centerX - 22, centerY - 22), \
# #                          (centerX + 22, centerY + 22), 2)
# #         pygame.draw.line(board, (0, 0, 0), (centerX + 22, centerY - 22), \
# #                          (centerX - 22, centerY + 22), 2)
# #
# #     # mark the space as used
# #     grid[boardRow][boardCol] = Piece
# #
# #
# # def clickBoard(board):
# #     # determine where the user clicked and if the space is not already
# #     # occupied, draw the appropriate piece there (X or O)
# #     # ---------------------------------------------------------------
# #     # board : the game board surface
# #
# #     global grid, XO
# #
# #     (mouseX, mouseY) = pygame.mouse.get_pos()
# #     (row, col) = boardPos(mouseX, mouseY)
# #
# #     # make sure no one's used this space
# #     if ((grid[row][col] == "X") or (grid[row][col] == "O")):
# #         # this space is in use
# #         return
# #
# #     # draw an X or O
# #     drawMove(board, row, col, XO)
# #
# #     # toggle XO to the other player's move
# #     if (XO == "X"):
# #         XO = "O"
# #     else:
# #         XO = "X"
# #
# #
# # def gameWon(board):
# #     # determine if anyone has won the game
# #     # ---------------------------------------------------------------
# #     # board : the game board surface
# #
# #     global grid, winner
# #
# #     # check for winning rows
# #     for row in range(0, 3):
# #         if ((grid[row][0] == grid[row][1] == grid[row][2]) and \
# #                 (grid[row][0] is not None)):
# #             # this row won
# #             winner = grid[row][0]
# #             pygame.draw.line(board, (250, 0, 0), (0, (row + 1) * 100 - 50), \
# #                              (300, (row + 1) * 100 - 50), 2)
# #             break
# #
# #     # check for winning columns
# #     for col in range(0, 3):
# #         if (grid[0][col] == grid[1][col] == grid[2][col]) and \
# #                 (grid[0][col] is not None):
# #             # this column won
# #             winner = grid[0][col]
# #             pygame.draw.line(board, (250, 0, 0), ((col + 1) * 100 - 50, 0), \
# #                              ((col + 1) * 100 - 50, 300), 2)
# #             break
# #
# #     # check for diagonal winners
# #     if (grid[0][0] == grid[1][1] == grid[2][2]) and \
# #             (grid[0][0] is not None):
# #         # game won diagonally left to right
# #         winner = grid[0][0]
# #         pygame.draw.line(board, (250, 0, 0), (50, 50), (250, 250), 2)
# #
# #     if (grid[0][2] == grid[1][1] == grid[2][0]) and \
# #             (grid[0][2] is not None):
# #         # game won diagonally right to left
# #         winner = grid[0][2]
# #         pygame.draw.line(board, (250, 0, 0), (250, 50), (50, 250), 2)
# #
# #
# # # --------------------------------------------------------------------
# # # initialize pygame and our window
# # pygame.init()
# # ttt = pygame.display.set_mode((300, 325))
# # pygame.display.set_caption('Tic-Tac-Toe')
# #
# # # create the game board
# # board = initBoard(ttt)
# #
# # # main event loop
# # running = 1
# #
#
# # while (running == 1):
# #     for event in pygame.event.get():
# #         if event.type is QUIT:
# #             running = 0
# #         elif event.type is MOUSEBUTTONDOWN:
# #             # the user clicked; place an X or O
# #             clickBoard(board)
# #
# #         # check for a winner
# #         gameWon(board)
# #
# #         # update the display
# #         showBoard(ttt, board)
# import sys, math
# import numpy as np
#
# import Box2D
# from Box2D.b2 import (edgeShape, circleShape, fixtureDef, polygonShape, revoluteJointDef, contactListener)
#
# import gym
# from gym import spaces
# from gym.envs.box2d.car_dynamics import Car
# from gym.utils import colorize, seeding, EzPickle
#
# import pyglet
# from pyglet import gl
#
# # Easiest continuous control task to learn from pixels, a top-down racing environment.
# # Discreet control is reasonable in this environment as well, on/off discretisation is
# # fine.
# #
# # State consists of STATE_W x STATE_H pixels.
# #
# # Reward is -0.1 every frame and +1000/N for every track tile visited, where N is
# # the total number of tiles in track. For example, if you have finished in 732 frames,
# # your reward is 1000 - 0.1*732 = 926.8 points.
# #
# # Game is solved when agent consistently gets 900+ points. Track is random every episode.
# #
# # Episode finishes when all tiles are visited. Car also can go outside of PLAYFIELD, that
# # is far off the track, then it will get -100 and die.
# #
# # Some indicators shown at the bottom of the window and the state RGB buffer. From
# # left to right: true speed, four ABS sensors, steering wheel position, gyroscope.
# #
# # To play yourself (it's rather fast for humans), type:
# #
# # python gym/envs/box2d/car_racing.py
# #
# # Remember it's powerful rear-wheel drive car, don't press accelerator and turn at the
# # same time.
# #
# # Created by Oleg Klimov. Licensed on the same terms as the rest of OpenAI Gym.
#
# STATE_W = 96   # less than Atari 160x192
# STATE_H = 96
# VIDEO_W = 600
# VIDEO_H = 400
# WINDOW_W = 1000
# WINDOW_H = 800
#
# SCALE       = 6.0        # Track scale
# TRACK_RAD   = 900/SCALE  # Track is heavily morphed circle with this radius
# PLAYFIELD   = 2000/SCALE # Game over boundary
# FPS         = 50
# ZOOM        = 2.7        # Camera zoom
# ZOOM_FOLLOW = True       # Set to False for fixed view (don't use zoom)
#
#
# TRACK_DETAIL_STEP = 21/SCALE
# TRACK_TURN_RATE = 0.31
# TRACK_WIDTH = 40/SCALE
# BORDER = 8/SCALE
# BORDER_MIN_COUNT = 4
#
# ROAD_COLOR = [0.4, 0.4, 0.4]
#
# class FrictionDetector(contactListener):
#     def __init__(self, env):
#         contactListener.__init__(self)
#         self.env = env
#     def BeginContact(self, contact):
#         self._contact(contact, True)
#     def EndContact(self, contact):
#         self._contact(contact, False)
#     def _contact(self, contact, begin):
#         tile = None
#         obj = None
#         u1 = contact.fixtureA.body.userData
#         u2 = contact.fixtureB.body.userData
#         if u1 and "road_friction" in u1.__dict__:
#             tile = u1
#             obj  = u2
#         if u2 and "road_friction" in u2.__dict__:
#             tile = u2
#             obj  = u1
#         if not tile: return
#
#         tile.color[0] = ROAD_COLOR[0]
#         tile.color[1] = ROAD_COLOR[1]
#         tile.color[2] = ROAD_COLOR[2]
#         if not obj or "tiles" not in obj.__dict__: return
#         if begin:
#             obj.tiles.add(tile)
#             #print tile.road_friction, "ADD", len(obj.tiles)
#             if not tile.road_visited:
#                 tile.road_visited = True
#                 self.env.reward += 1000.0/len(self.env.track)
#                 self.env.tile_visited_count += 1
#         else:
#             obj.tiles.remove(tile)
#             #print tile.road_friction, "DEL", len(obj.tiles) -- should delete to zero when on grass (this works)
#
# class CarRacing(gym.Env, EzPickle):
#     metadata = {
#         'render.modes': ['human', 'rgb_array', 'state_pixels'],
#         'video.frames_per_second' : FPS
#     }
#
#     def __init__(self, verbose=1):
#         EzPickle.__init__(self)
#         self.seed()
#         self.contactListener_keepref = FrictionDetector(self)
#         self.world = Box2D.b2World((0,0), contactListener=self.contactListener_keepref)
#         self.viewer = None
#         self.invisible_state_window = None
#         self.invisible_video_window = None
#         self.road = None
#         self.car = None
#         self.reward = 0.0
#         self.prev_reward = 0.0
#         self.verbose = verbose
#
#         self.action_space = spaces.Box( np.array([-1,0,0]), np.array([+1,+1,+1]), dtype=np.float32)  # steer, gas, brake
#         self.observation_space = spaces.Box(low=0, high=255, shape=(STATE_H, STATE_W, 3), dtype=np.uint8)
#
#     def seed(self, seed=None):
#         self.np_random, seed = seeding.np_random(seed)
#         return [seed]
#
#     def _destroy(self):
#         if not self.road: return
#         for t in self.road:
#             self.world.DestroyBody(t)
#         self.road = []
#         self.car.destroy()
#
#     def _create_track(self):
#         CHECKPOINTS = 12
#
#         # Create checkpoints
#         checkpoints = []
#         for c in range(CHECKPOINTS):
#             alpha = 2*math.pi*c/CHECKPOINTS + self.np_random.uniform(0, 2*math.pi*1/CHECKPOINTS)
#             rad = self.np_random.uniform(TRACK_RAD/3, TRACK_RAD)
#             if c==0:
#                 alpha = 0
#                 rad = 1.5*TRACK_RAD
#             if c==CHECKPOINTS-1:
#                 alpha = 2*math.pi*c/CHECKPOINTS
#                 self.start_alpha = 2*math.pi*(-0.5)/CHECKPOINTS
#                 rad = 1.5*TRACK_RAD
#             checkpoints.append( (alpha, rad*math.cos(alpha), rad*math.sin(alpha)) )
#
#         #print "\n".join(str(h) for h in checkpoints)
#         #self.road_poly = [ (    # uncomment this to see checkpoints
#         #    [ (tx,ty) for a,tx,ty in checkpoints ],
#         #    (0.7,0.7,0.9) ) ]
#         self.road = []
#
#         # Go from one checkpoint to another to create track
#         x, y, beta = 1.5*TRACK_RAD, 0, 0
#         dest_i = 0
#         laps = 0
#         track = []
#         no_freeze = 2500
#         visited_other_side = False
#         while 1:
#             alpha = math.atan2(y, x)
#             if visited_other_side and alpha > 0:
#                 laps += 1
#                 visited_other_side = False
#             if alpha < 0:
#                 visited_other_side = True
#                 alpha += 2*math.pi
#             while True: # Find destination from checkpoints
#                 failed = True
#                 while True:
#                     dest_alpha, dest_x, dest_y = checkpoints[dest_i % len(checkpoints)]
#                     if alpha <= dest_alpha:
#                         failed = False
#                         break
#                     dest_i += 1
#                     if dest_i % len(checkpoints) == 0: break
#                 if not failed: break
#                 alpha -= 2*math.pi
#                 continue
#             r1x = math.cos(beta)
#             r1y = math.sin(beta)
#             p1x = -r1y
#             p1y = r1x
#             dest_dx = dest_x - x  # vector towards destination
#             dest_dy = dest_y - y
#             proj = r1x*dest_dx + r1y*dest_dy  # destination vector projected on rad
#             while beta - alpha >  1.5*math.pi: beta -= 2*math.pi
#             while beta - alpha < -1.5*math.pi: beta += 2*math.pi
#             prev_beta = beta
#             proj *= SCALE
#             if proj >  0.3: beta -= min(TRACK_TURN_RATE, abs(0.001*proj))
#             if proj < -0.3: beta += min(TRACK_TURN_RATE, abs(0.001*proj))
#             x += p1x*TRACK_DETAIL_STEP
#             y += p1y*TRACK_DETAIL_STEP
#             track.append( (alpha,prev_beta*0.5 + beta*0.5,x,y) )
#             if laps > 4: break
#             no_freeze -= 1
#             if no_freeze==0: break
#         #print "\n".join([str(t) for t in enumerate(track)])
#
#         # Find closed loop range i1..i2, first loop should be ignored, second is OK
#         i1, i2 = -1, -1
#         i = len(track)
#         while True:
#             i -= 1
#             if i==0: return False  # Failed
#             pass_through_start = track[i][0] > self.start_alpha and track[i-1][0] <= self.start_alpha
#             if pass_through_start and i2==-1:
#                 i2 = i
#             elif pass_through_start and i1==-1:
#                 i1 = i
#                 break
#         if self.verbose == 1:
#             print("Track generation: %i..%i -> %i-tiles track" % (i1, i2, i2-i1))
#         assert i1!=-1
#         assert i2!=-1
#
#         track = track[i1:i2-1]
#
#         first_beta = track[0][1]
#         first_perp_x = math.cos(first_beta)
#         first_perp_y = math.sin(first_beta)
#         # Length of perpendicular jump to put together head and tail
#         well_glued_together = np.sqrt(
#             np.square( first_perp_x*(track[0][2] - track[-1][2]) ) +
#             np.square( first_perp_y*(track[0][3] - track[-1][3]) ))
#         if well_glued_together > TRACK_DETAIL_STEP:
#             return False
#
#         # Red-white border on hard turns
#         border = [False]*len(track)
#         for i in range(len(track)):
#             good = True
#             oneside = 0
#             for neg in range(BORDER_MIN_COUNT):
#                 beta1 = track[i-neg-0][1]
#                 beta2 = track[i-neg-1][1]
#                 good &= abs(beta1 - beta2) > TRACK_TURN_RATE*0.2
#                 oneside += np.sign(beta1 - beta2)
#             good &= abs(oneside) == BORDER_MIN_COUNT
#             border[i] = good
#         for i in range(len(track)):
#             for neg in range(BORDER_MIN_COUNT):
#                 border[i-neg] |= border[i]
#
#         # Create tiles
#         for i in range(len(track)):
#             alpha1, beta1, x1, y1 = track[i]
#             alpha2, beta2, x2, y2 = track[i-1]
#             road1_l = (x1 - TRACK_WIDTH*math.cos(beta1), y1 - TRACK_WIDTH*math.sin(beta1))
#             road1_r = (x1 + TRACK_WIDTH*math.cos(beta1), y1 + TRACK_WIDTH*math.sin(beta1))
#             road2_l = (x2 - TRACK_WIDTH*math.cos(beta2), y2 - TRACK_WIDTH*math.sin(beta2))
#             road2_r = (x2 + TRACK_WIDTH*math.cos(beta2), y2 + TRACK_WIDTH*math.sin(beta2))
#             t = self.world.CreateStaticBody( fixtures = fixtureDef(
#                 shape=polygonShape(vertices=[road1_l, road1_r, road2_r, road2_l])
#                 ))
#             t.userData = t
#             c = 0.01*(i%3)
#             t.color = [ROAD_COLOR[0] + c, ROAD_COLOR[1] + c, ROAD_COLOR[2] + c]
#             t.road_visited = False
#             t.road_friction = 1.0
#             t.fixtures[0].sensor = True
#             self.road_poly.append(( [road1_l, road1_r, road2_r, road2_l], t.color ))
#             self.road.append(t)
#             if border[i]:
#                 side = np.sign(beta2 - beta1)
#                 b1_l = (x1 + side* TRACK_WIDTH        *math.cos(beta1), y1 + side* TRACK_WIDTH        *math.sin(beta1))
#                 b1_r = (x1 + side*(TRACK_WIDTH+BORDER)*math.cos(beta1), y1 + side*(TRACK_WIDTH+BORDER)*math.sin(beta1))
#                 b2_l = (x2 + side* TRACK_WIDTH        *math.cos(beta2), y2 + side* TRACK_WIDTH        *math.sin(beta2))
#                 b2_r = (x2 + side*(TRACK_WIDTH+BORDER)*math.cos(beta2), y2 + side*(TRACK_WIDTH+BORDER)*math.sin(beta2))
#                 self.road_poly.append(( [b1_l, b1_r, b2_r, b2_l], (1,1,1) if i%2==0 else (1,0,0) ))
#         self.track = track
#         return True
#
#     def reset(self):
#         self._destroy()
#         self.reward = 0.0
#         self.prev_reward = 0.0
#         self.tile_visited_count = 0
#         self.t = 0.0
#         self.road_poly = []
#
#         while True:
#             success = self._create_track()
#             if success: break
#             if self.verbose == 1:
#                 print("retry to generate track (normal if there are not many of this messages)")
#         self.car = Car(self.world, *self.track[0][1:4])
#
#         return self.step(None)[0]
#
#     def step(self, action):
#         if action is not None:
#             self.car.steer(-action[0])
#             self.car.gas(action[1])
#             self.car.brake(action[2])
#
#         self.car.step(1.0/FPS)
#         self.world.Step(1.0/FPS, 6*30, 2*30)
#         self.t += 1.0/FPS
#
#         self.state = self.render("state_pixels")
#
#         step_reward = 0
#         done = False
#         if action is not None: # First step without action, called from reset()
#             self.reward -= 0.1
#             # We actually don't want to count fuel spent, we want car to be faster.
#             #self.reward -=  10 * self.car.fuel_spent / ENGINE_POWER
#             self.car.fuel_spent = 0.0
#             step_reward = self.reward - self.prev_reward
#             self.prev_reward = self.reward
#             if self.tile_visited_count==len(self.track):
#                 done = True
#             x, y = self.car.hull.position
#             if abs(x) > PLAYFIELD or abs(y) > PLAYFIELD:
#                 done = True
#                 step_reward = -100
#
#         return self.state, step_reward, done, {}
#
#     def render(self, mode='human'):
#         assert mode in ['human', 'state_pixels', 'rgb_array']
#         if self.viewer is None:
#             from gym.envs.classic_control import rendering
#             self.viewer = rendering.Viewer(WINDOW_W, WINDOW_H)
#             self.score_label = pyglet.text.Label('0000', font_size=36,
#                 x=20, y=WINDOW_H*2.5/40.00, anchor_x='left', anchor_y='center',
#                 color=(255,255,255,255))
#             self.transform = rendering.Transform()
#
#         if "t" not in self.__dict__: return  # reset() not called yet
#
#         zoom = 0.1*SCALE*max(1-self.t, 0) + ZOOM*SCALE*min(self.t, 1)   # Animate zoom first second
#         zoom_state  = ZOOM*SCALE*STATE_W/WINDOW_W
#         zoom_video  = ZOOM*SCALE*VIDEO_W/WINDOW_W
#         scroll_x = self.car.hull.position[0]
#         scroll_y = self.car.hull.position[1]
#         angle = -self.car.hull.angle
#         vel = self.car.hull.linearVelocity
#         if np.linalg.norm(vel) > 0.5:
#             angle = math.atan2(vel[0], vel[1])
#         self.transform.set_scale(zoom, zoom)
#         self.transform.set_translation(
#             WINDOW_W/2 - (scroll_x*zoom*math.cos(angle) - scroll_y*zoom*math.sin(angle)),
#             WINDOW_H/4 - (scroll_x*zoom*math.sin(angle) + scroll_y*zoom*math.cos(angle)) )
#         self.transform.set_rotation(angle)
#
#         self.car.draw(self.viewer, mode!="state_pixels")
#
#         arr = None
#         win = self.viewer.window
#         win.switch_to()
#         win.dispatch_events()
#
#         win.clear()
#         t = self.transform
#         if mode=='rgb_array':
#             VP_W = VIDEO_W
#             VP_H = VIDEO_H
#         elif mode == 'state_pixels':
#             VP_W = STATE_W
#             VP_H = STATE_H
#         else:
#             pixel_scale = 1
#             if hasattr(win.context, '_nscontext'):
#                 pixel_scale = win.context._nscontext.view().backingScaleFactor()  # pylint: disable=protected-access
#             VP_W = pixel_scale * WINDOW_W
#             VP_H = pixel_scale * WINDOW_H
#
#         gl.glViewport(0, 0, VP_W, VP_H)
#         t.enable()
#         self.render_road()
#         for geom in self.viewer.onetime_geoms:
#             geom.render()
#         self.viewer.onetime_geoms = []
#         t.disable()
#         self.render_indicators(WINDOW_W, WINDOW_H)
#
#         if mode == 'human':
#             win.flip()
#             return self.viewer.isopen
#
#         image_data = pyglet.image.get_buffer_manager().get_color_buffer().get_image_data()
#         arr = np.fromstring(image_data.data, dtype=np.uint8, sep='')
#         arr = arr.reshape(VP_H, VP_W, 4)
#         arr = arr[::-1, :, 0:3]
#
#         return arr
#
#     def close(self):
#         if self.viewer is not None:
#             self.viewer.close()
#             self.viewer = None
#
#     def render_road(self):
#         gl.glBegin(gl.GL_QUADS)
#         gl.glColor4f(0.4, 0.8, 0.4, 1.0)
#         gl.glVertex3f(-PLAYFIELD, +PLAYFIELD, 0)
#         gl.glVertex3f(+PLAYFIELD, +PLAYFIELD, 0)
#         gl.glVertex3f(+PLAYFIELD, -PLAYFIELD, 0)
#         gl.glVertex3f(-PLAYFIELD, -PLAYFIELD, 0)
#         gl.glColor4f(0.4, 0.9, 0.4, 1.0)
#         k = PLAYFIELD/20.0
#         for x in range(-20, 20, 2):
#             for y in range(-20, 20, 2):
#                 gl.glVertex3f(k*x + k, k*y + 0, 0)
#                 gl.glVertex3f(k*x + 0, k*y + 0, 0)
#                 gl.glVertex3f(k*x + 0, k*y + k, 0)
#                 gl.glVertex3f(k*x + k, k*y + k, 0)
#         for poly, color in self.road_poly:
#             gl.glColor4f(color[0], color[1], color[2], 1)
#             for p in poly:
#                 gl.glVertex3f(p[0], p[1], 0)
#         gl.glEnd()
#
#     def render_indicators(self, W, H):
#         gl.glBegin(gl.GL_QUADS)
#         s = W/40.0
#         h = H/40.0
#         gl.glColor4f(0,0,0,1)
#         gl.glVertex3f(W, 0, 0)
#         gl.glVertex3f(W, 5*h, 0)
#         gl.glVertex3f(0, 5*h, 0)
#         gl.glVertex3f(0, 0, 0)
#         def vertical_ind(place, val, color):
#             gl.glColor4f(color[0], color[1], color[2], 1)
#             gl.glVertex3f((place+0)*s, h + h*val, 0)
#             gl.glVertex3f((place+1)*s, h + h*val, 0)
#             gl.glVertex3f((place+1)*s, h, 0)
#             gl.glVertex3f((place+0)*s, h, 0)
#         def horiz_ind(place, val, color):
#             gl.glColor4f(color[0], color[1], color[2], 1)
#             gl.glVertex3f((place+0)*s, 4*h , 0)
#             gl.glVertex3f((place+val)*s, 4*h, 0)
#             gl.glVertex3f((place+val)*s, 2*h, 0)
#             gl.glVertex3f((place+0)*s, 2*h, 0)
#         true_speed = np.sqrt(np.square(self.car.hull.linearVelocity[0]) + np.square(self.car.hull.linearVelocity[1]))
#         vertical_ind(5, 0.02*true_speed, (1,1,1))
#         vertical_ind(7, 0.01*self.car.wheels[0].omega, (0.0,0,1)) # ABS sensors
#         vertical_ind(8, 0.01*self.car.wheels[1].omega, (0.0,0,1))
#         vertical_ind(9, 0.01*self.car.wheels[2].omega, (0.2,0,1))
#         vertical_ind(10,0.01*self.car.wheels[3].omega, (0.2,0,1))
#         horiz_ind(20, -10.0*self.car.wheels[0].joint.angle, (0,1,0))
#         horiz_ind(30, -0.8*self.car.hull.angularVelocity, (1,0,0))
#         gl.glEnd()
#         self.score_label.text = "%04i" % self.reward
#         self.score_label.draw()
#
#
# if __name__=="__main__":
#     from pyglet.window import key
#     a = np.array( [0.0, 0.0, 0.0] )
#     def key_press(k, mod):
#         global restart
#         if k==0xff0d: restart = True
#         if k==key.LEFT:  a[0] = -1.0
#         if k==key.RIGHT: a[0] = +1.0
#         if k==key.UP:    a[1] = +1.0
#         if k==key.DOWN:  a[2] = +0.8   # set 1.0 for wheels to block to zero rotation
#     def key_release(k, mod):
#         if k==key.LEFT  and a[0]==-1.0: a[0] = 0
#         if k==key.RIGHT and a[0]==+1.0: a[0] = 0
#         if k==key.UP:    a[1] = 0
#         if k==key.DOWN:  a[2] = 0
#     env = CarRacing()
#     env.render()
#     env.viewer.window.on_key_press = key_press
#     env.viewer.window.on_key_release = key_release
#     record_video = False
#     if record_video:
#         from gym.wrappers.monitor import Monitor
#         env = Monitor(env, '/tmp/video-test', force=True)
#     isopen = True
#     while isopen:
#         env.reset()
#         total_reward = 0.0
#         steps = 0
#         restart = False
#         while True:
#             s, r, done, info = env.step(a)
#             total_reward += r
#             if steps % 200 == 0 or done:
#                 print("\naction " + str(["{:+0.2f}".format(x) for x in a]))
#                 print("step {} total_reward {:+0.2f}".format(steps, total_reward))
#                 #import matplotlib.pyplot as plt
#                 #plt.imshow(s)
#                 #plt.savefig("test.jpeg")
#             steps += 1
#             isopen = env.render()
#             if done or restart or isopen == False: break
#     env.close()
import sys, math
import numpy as np

import Box2D
from Box2D.b2 import (edgeShape, circleShape, fixtureDef, polygonShape, revoluteJointDef, contactListener)

import gym
from gym import spaces
from gym.envs.box2d.car_dynamics import Car
from gym.utils import colorize, seeding, EzPickle

import pyglet
from pyglet import gl

# Easiest continuous control task to learn from pixels, a top-down racing environment.
# Discreet control is reasonable in this environment as well, on/off discretisation is
# fine.
#
# State consists of STATE_W x STATE_H pixels.
#
# Reward is -0.1 every frame and +1000/N for every track tile visited, where N is
# the total number of tiles in track. For example, if you have finished in 732 frames,
# your reward is 1000 - 0.1*732 = 926.8 points.
#
# Game is solved when agent consistently gets 900+ points. Track is random every episode.
#
# Episode finishes when all tiles are visited. Car also can go outside of PLAYFIELD, that
# is far off the track, then it will get -100 and die.
#
# Some indicators shown at the bottom of the window and the state RGB buffer. From
# left to right: true speed, four ABS sensors, steering wheel position, gyroscope.
#
# To play yourself (it's rather fast for humans), type:
#
# python gym/envs/box2d/car_racing.py
#
# Remember it's powerful rear-wheel drive car, don't press accelerator and turn at the
# same time.
#
# Created by Oleg Klimov. Licensed on the same terms as the rest of OpenAI Gym.

STATE_W = 96   # less than Atari 160x192
STATE_H = 96
VIDEO_W = 600
VIDEO_H = 400
WINDOW_W = 1000
WINDOW_H = 800

SCALE       = 6.0        # Track scale
TRACK_RAD   = 900/SCALE  # Track is heavily morphed circle with this radius
PLAYFIELD   = 2000/SCALE # Game over boundary
FPS         = 50
ZOOM        = 2.7        # Camera zoom
ZOOM_FOLLOW = True       # Set to False for fixed view (don't use zoom)


TRACK_DETAIL_STEP = 21/SCALE
TRACK_TURN_RATE = 0.31
TRACK_WIDTH = 40/SCALE
BORDER = 8/SCALE
BORDER_MIN_COUNT = 4

ROAD_COLOR = [0.4, 0.4, 0.4]

class FrictionDetector(contactListener):
    def __init__(self, env):
        contactListener.__init__(self)
        self.env = env
    def BeginContact(self, contact):
        self._contact(contact, True)
    def EndContact(self, contact):
        self._contact(contact, False)
    def _contact(self, contact, begin):
        tile = None
        obj = None
        u1 = contact.fixtureA.body.userData
        u2 = contact.fixtureB.body.userData
        if u1 and "road_friction" in u1.__dict__:
            tile = u1
            obj  = u2
        if u2 and "road_friction" in u2.__dict__:
            tile = u2
            obj  = u1
        if not tile: return

        tile.color[0] = ROAD_COLOR[0]
        tile.color[1] = ROAD_COLOR[1]
        tile.color[2] = ROAD_COLOR[2]
        if not obj or "tiles" not in obj.__dict__: return
        if begin:
            obj.tiles.add(tile)
            #print tile.road_friction, "ADD", len(obj.tiles)
            if not tile.road_visited:
                tile.road_visited = True
                self.env.reward += 1000.0/len(self.env.track)
                self.env.tile_visited_count += 1
        else:
            obj.tiles.remove(tile)
            #print tile.road_friction, "DEL", len(obj.tiles) -- should delete to zero when on grass (this works)

class CarRacing(gym.Env, EzPickle):
    metadata = {
        'render.modes': ['human', 'rgb_array', 'state_pixels'],
        'video.frames_per_second' : FPS
    }

    def __init__(self, verbose=1):
        EzPickle.__init__(self)
        self.seed()
        self.contactListener_keepref = FrictionDetector(self)
        self.world = Box2D.b2World((0,0), contactListener=self.contactListener_keepref)
        self.viewer = None
        self.invisible_state_window = None
        self.invisible_video_window = None
        self.road = None
        self.car = None
        self.reward = 0.0
        self.prev_reward = 0.0
        self.verbose = verbose

        self.action_space = spaces.Box( np.array([-1,0,0]), np.array([+1,+1,+1]), dtype=np.float32)  # steer, gas, brake
        self.observation_space = spaces.Box(low=0, high=255, shape=(STATE_H, STATE_W, 3), dtype=np.uint8)

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def _destroy(self):
        if not self.road: return
        for t in self.road:
            self.world.DestroyBody(t)
        self.road = []
        self.car.destroy()

    def _create_track(self):
        CHECKPOINTS = 12

        # Create checkpoints
        checkpoints = []
        for c in range(CHECKPOINTS):
            alpha = 2*math.pi*c/CHECKPOINTS + self.np_random.uniform(0, 2*math.pi*1/CHECKPOINTS)
            rad = self.np_random.uniform(TRACK_RAD/3, TRACK_RAD)
            if c==0:
                alpha = 0
                rad = 1.5*TRACK_RAD
            if c==CHECKPOINTS-1:
                alpha = 2*math.pi*c/CHECKPOINTS
                self.start_alpha = 2*math.pi*(-0.5)/CHECKPOINTS
                rad = 1.5*TRACK_RAD
            checkpoints.append( (alpha, rad*math.cos(alpha), rad*math.sin(alpha)) )

        #print "\n".join(str(h) for h in checkpoints)
        #self.road_poly = [ (    # uncomment this to see checkpoints
        #    [ (tx,ty) for a,tx,ty in checkpoints ],
        #    (0.7,0.7,0.9) ) ]
        self.road = []

        # Go from one checkpoint to another to create track
        x, y, beta = 1.5*TRACK_RAD, 0, 0
        dest_i = 0
        laps = 0
        track = []
        no_freeze = 2500
        visited_other_side = False
        while 1:
            alpha = math.atan2(y, x)
            if visited_other_side and alpha > 0:
                laps += 1
                visited_other_side = False
            if alpha < 0:
                visited_other_side = True
                alpha += 2*math.pi
            while True: # Find destination from checkpoints
                failed = True
                while True:
                    dest_alpha, dest_x, dest_y = checkpoints[dest_i % len(checkpoints)]
                    if alpha <= dest_alpha:
                        failed = False
                        break
                    dest_i += 1
                    if dest_i % len(checkpoints) == 0: break
                if not failed: break
                alpha -= 2*math.pi
                continue
            r1x = math.cos(beta)
            r1y = math.sin(beta)
            p1x = -r1y
            p1y = r1x
            dest_dx = dest_x - x  # vector towards destination
            dest_dy = dest_y - y
            proj = r1x*dest_dx + r1y*dest_dy  # destination vector projected on rad
            while beta - alpha >  1.5*math.pi: beta -= 2*math.pi
            while beta - alpha < -1.5*math.pi: beta += 2*math.pi
            prev_beta = beta
            proj *= SCALE
            if proj >  0.3: beta -= min(TRACK_TURN_RATE, abs(0.001*proj))
            if proj < -0.3: beta += min(TRACK_TURN_RATE, abs(0.001*proj))
            x += p1x*TRACK_DETAIL_STEP
            y += p1y*TRACK_DETAIL_STEP
            track.append( (alpha,prev_beta*0.5 + beta*0.5,x,y) )
            if laps > 4: break
            no_freeze -= 1
            if no_freeze==0: break
        #print "\n".join([str(t) for t in enumerate(track)])

        # Find closed loop range i1..i2, first loop should be ignored, second is OK
        i1, i2 = -1, -1
        i = len(track)
        while True:
            i -= 1
            if i==0: return False  # Failed
            pass_through_start = track[i][0] > self.start_alpha and track[i-1][0] <= self.start_alpha
            if pass_through_start and i2==-1:
                i2 = i
            elif pass_through_start and i1==-1:
                i1 = i
                break
        if self.verbose == 1:
            print("Track generation: %i..%i -> %i-tiles track" % (i1, i2, i2-i1))
        assert i1!=-1
        assert i2!=-1

        track = track[i1:i2-1]

        first_beta = track[0][1]
        first_perp_x = math.cos(first_beta)
        first_perp_y = math.sin(first_beta)
        # Length of perpendicular jump to put together head and tail
        well_glued_together = np.sqrt(
            np.square( first_perp_x*(track[0][2] - track[-1][2]) ) +
            np.square( first_perp_y*(track[0][3] - track[-1][3]) ))
        if well_glued_together > TRACK_DETAIL_STEP:
            return False

        # Red-white border on hard turns
        border = [False]*len(track)
        for i in range(len(track)):
            good = True
            oneside = 0
            for neg in range(BORDER_MIN_COUNT):
                beta1 = track[i-neg-0][1]
                beta2 = track[i-neg-1][1]
                good &= abs(beta1 - beta2) > TRACK_TURN_RATE*0.2
                oneside += np.sign(beta1 - beta2)
            good &= abs(oneside) == BORDER_MIN_COUNT
            border[i] = good
        for i in range(len(track)):
            for neg in range(BORDER_MIN_COUNT):
                border[i-neg] |= border[i]

        # Create tiles
        for i in range(len(track)):
            alpha1, beta1, x1, y1 = track[i]
            alpha2, beta2, x2, y2 = track[i-1]
            road1_l = (x1 - TRACK_WIDTH*math.cos(beta1), y1 - TRACK_WIDTH*math.sin(beta1))
            road1_r = (x1 + TRACK_WIDTH*math.cos(beta1), y1 + TRACK_WIDTH*math.sin(beta1))
            road2_l = (x2 - TRACK_WIDTH*math.cos(beta2), y2 - TRACK_WIDTH*math.sin(beta2))
            road2_r = (x2 + TRACK_WIDTH*math.cos(beta2), y2 + TRACK_WIDTH*math.sin(beta2))
            t = self.world.CreateStaticBody( fixtures = fixtureDef(
                shape=polygonShape(vertices=[road1_l, road1_r, road2_r, road2_l])
                ))
            t.userData = t
            c = 0.01*(i%3)
            t.color = [ROAD_COLOR[0] + c, ROAD_COLOR[1] + c, ROAD_COLOR[2] + c]
            t.road_visited = False
            t.road_friction = 1.0
            t.fixtures[0].sensor = True
            self.road_poly.append(( [road1_l, road1_r, road2_r, road2_l], t.color ))
            self.road.append(t)
            if border[i]:
                side = np.sign(beta2 - beta1)
                b1_l = (x1 + side* TRACK_WIDTH        *math.cos(beta1), y1 + side* TRACK_WIDTH        *math.sin(beta1))
                b1_r = (x1 + side*(TRACK_WIDTH+BORDER)*math.cos(beta1), y1 + side*(TRACK_WIDTH+BORDER)*math.sin(beta1))
                b2_l = (x2 + side* TRACK_WIDTH        *math.cos(beta2), y2 + side* TRACK_WIDTH        *math.sin(beta2))
                b2_r = (x2 + side*(TRACK_WIDTH+BORDER)*math.cos(beta2), y2 + side*(TRACK_WIDTH+BORDER)*math.sin(beta2))
                self.road_poly.append(( [b1_l, b1_r, b2_r, b2_l], (1,1,1) if i%2==0 else (1,0,0) ))
        self.track = track
        return True

    def reset(self):
        self._destroy()
        self.reward = 0.0
        self.prev_reward = 0.0
        self.tile_visited_count = 0
        self.t = 0.0
        self.road_poly = []

        while True:
            success = self._create_track()
            if success: break
            if self.verbose == 1:
                print("retry to generate track (normal if there are not many of this messages)")
        self.car = Car(self.world, *self.track[0][1:4])

        return self.step(None)[0]

    def step(self, action):
        if action is not None:
            self.car.steer(-action[0])
            self.car.gas(action[1])
            self.car.brake(action[2])

        self.car.step(1.0/FPS)
        self.world.Step(1.0/FPS, 6*30, 2*30)
        self.t += 1.0/FPS

        self.state = self.render("state_pixels")

        step_reward = 0
        done = False
        if action is not None: # First step without action, called from reset()
            self.reward -= 0.1
            # We actually don't want to count fuel spent, we want car to be faster.
            #self.reward -=  10 * self.car.fuel_spent / ENGINE_POWER
            self.car.fuel_spent = 0.0
            step_reward = self.reward - self.prev_reward
            self.prev_reward = self.reward
            if self.tile_visited_count==len(self.track):
                done = True
            x, y = self.car.hull.position
            if abs(x) > PLAYFIELD or abs(y) > PLAYFIELD:
                done = True
                step_reward = -100

        return self.state, step_reward, done, {}

    def render(self, mode='human'):
        assert mode in ['human', 'state_pixels', 'rgb_array']
        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.Viewer(WINDOW_W, WINDOW_H)
            self.score_label = pyglet.text.Label('0000', font_size=36,
                x=20, y=WINDOW_H*2.5/40.00, anchor_x='left', anchor_y='center',
                color=(255,255,255,255))
            self.transform = rendering.Transform()

        if "t" not in self.__dict__: return  # reset() not called yet

        zoom = 0.1*SCALE*max(1-self.t, 0) + ZOOM*SCALE*min(self.t, 1)   # Animate zoom first second
        zoom_state  = ZOOM*SCALE*STATE_W/WINDOW_W
        zoom_video  = ZOOM*SCALE*VIDEO_W/WINDOW_W
        scroll_x = self.car.hull.position[0]
        scroll_y = self.car.hull.position[1]
        angle = -self.car.hull.angle
        vel = self.car.hull.linearVelocity
        if np.linalg.norm(vel) > 0.5:
            angle = math.atan2(vel[0], vel[1])
        self.transform.set_scale(zoom, zoom)
        self.transform.set_translation(
            WINDOW_W/2 - (scroll_x*zoom*math.cos(angle) - scroll_y*zoom*math.sin(angle)),
            WINDOW_H/4 - (scroll_x*zoom*math.sin(angle) + scroll_y*zoom*math.cos(angle)) )
        self.transform.set_rotation(angle)

        self.car.draw(self.viewer, mode!="state_pixels")

        arr = None
        win = self.viewer.window
        win.switch_to()
        win.dispatch_events()

        win.clear()
        t = self.transform
        if mode=='rgb_array':
            VP_W = VIDEO_W
            VP_H = VIDEO_H
        elif mode == 'state_pixels':
            VP_W = STATE_W
            VP_H = STATE_H
        else:
            pixel_scale = 1
            if hasattr(win.context, '_nscontext'):
                pixel_scale = win.context._nscontext.view().backingScaleFactor()  # pylint: disable=protected-access
            VP_W = pixel_scale * WINDOW_W
            VP_H = pixel_scale * WINDOW_H

        gl.glViewport(0, 0, VP_W, VP_H)
        t.enable()
        self.render_road()
        for geom in self.viewer.onetime_geoms:
            geom.render()
        self.viewer.onetime_geoms = []
        t.disable()
        self.render_indicators(WINDOW_W, WINDOW_H)

        if mode == 'human':
            win.flip()
            return self.viewer.isopen

        image_data = pyglet.image.get_buffer_manager().get_color_buffer().get_image_data()
        arr = np.fromstring(image_data.data, dtype=np.uint8, sep='')
        arr = arr.reshape(VP_H, VP_W, 4)
        arr = arr[::-1, :, 0:3]

        return arr

    def close(self):
        if self.viewer is not None:
            self.viewer.close()
            self.viewer = None

    def render_road(self):
        gl.glBegin(gl.GL_QUADS)
        gl.glColor4f(0.4, 0.8, 0.4, 1.0)
        gl.glVertex3f(-PLAYFIELD, +PLAYFIELD, 0)
        gl.glVertex3f(+PLAYFIELD, +PLAYFIELD, 0)
        gl.glVertex3f(+PLAYFIELD, -PLAYFIELD, 0)
        gl.glVertex3f(-PLAYFIELD, -PLAYFIELD, 0)
        gl.glColor4f(0.4, 0.9, 0.4, 1.0)
        k = PLAYFIELD/20.0
        for x in range(-20, 20, 2):
            for y in range(-20, 20, 2):
                gl.glVertex3f(k*x + k, k*y + 0, 0)
                gl.glVertex3f(k*x + 0, k*y + 0, 0)
                gl.glVertex3f(k*x + 0, k*y + k, 0)
                gl.glVertex3f(k*x + k, k*y + k, 0)
        for poly, color in self.road_poly:
            gl.glColor4f(color[0], color[1], color[2], 1)
            for p in poly:
                gl.glVertex3f(p[0], p[1], 0)
        gl.glEnd()

    def render_indicators(self, W, H):
        gl.glBegin(gl.GL_QUADS)
        s = W/40.0
        h = H/40.0
        gl.glColor4f(0,0,0,1)
        gl.glVertex3f(W, 0, 0)
        gl.glVertex3f(W, 5*h, 0)
        gl.glVertex3f(0, 5*h, 0)
        gl.glVertex3f(0, 0, 0)
        def vertical_ind(place, val, color):
            gl.glColor4f(color[0], color[1], color[2], 1)
            gl.glVertex3f((place+0)*s, h + h*val, 0)
            gl.glVertex3f((place+1)*s, h + h*val, 0)
            gl.glVertex3f((place+1)*s, h, 0)
            gl.glVertex3f((place+0)*s, h, 0)
        def horiz_ind(place, val, color):
            gl.glColor4f(color[0], color[1], color[2], 1)
            gl.glVertex3f((place+0)*s, 4*h , 0)
            gl.glVertex3f((place+val)*s, 4*h, 0)
            gl.glVertex3f((place+val)*s, 2*h, 0)
            gl.glVertex3f((place+0)*s, 2*h, 0)
        true_speed = np.sqrt(np.square(self.car.hull.linearVelocity[0]) + np.square(self.car.hull.linearVelocity[1]))
        vertical_ind(5, 0.02*true_speed, (1,1,1))
        vertical_ind(7, 0.01*self.car.wheels[0].omega, (0.0,0,1)) # ABS sensors
        vertical_ind(8, 0.01*self.car.wheels[1].omega, (0.0,0,1))
        vertical_ind(9, 0.01*self.car.wheels[2].omega, (0.2,0,1))
        vertical_ind(10,0.01*self.car.wheels[3].omega, (0.2,0,1))
        horiz_ind(20, -10.0*self.car.wheels[0].joint.angle, (0,1,0))
        horiz_ind(30, -0.8*self.car.hull.angularVelocity, (1,0,0))
        gl.glEnd()
        self.score_label.text = "%04i" % self.reward
        self.score_label.draw()


if __name__=="__main__":
    from pyglet.window import key
    a = np.array( [0.0, 0.0, 0.0] )
    def key_press(k, mod):
        global restart
        if k==0xff0d: restart = True
        if k==key.LEFT:  a[0] = -1.0
        if k==key.RIGHT: a[0] = +1.0
        if k==key.UP:    a[1] = +1.0
        if k==key.DOWN:  a[2] = +0.8   # set 1.0 for wheels to block to zero rotation
    def key_release(k, mod):
        if k==key.LEFT  and a[0]==-1.0: a[0] = 0
        if k==key.RIGHT and a[0]==+1.0: a[0] = 0
        if k==key.UP:    a[1] = 0
        if k==key.DOWN:  a[2] = 0
    env = CarRacing()
    env.render()
    env.viewer.window.on_key_press = key_press
    env.viewer.window.on_key_release = key_release
    record_video = False
    if record_video:
        from gym.wrappers.monitor import Monitor
        env = Monitor(env, '/tmp/video-test', force=True)
    isopen = True
    while isopen:
        env.reset()
        total_reward = 0.0
        steps = 0
        restart = False
        while True:
            s, r, done, info = env.step(a)
            total_reward += r
            if steps % 200 == 0 or done:
                print("\naction " + str(["{:+0.2f}".format(x) for x in a]))
                print("step {} total_reward {:+0.2f}".format(steps, total_reward))
                #import matplotlib.pyplot as plt
                #plt.imshow(s)
                #plt.savefig("test.jpeg")
            steps += 1
            isopen = env.render()
            if done or restart or isopen == False: break
    env.close()