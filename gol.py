#!/usr/bin/python
import sys
import random
import time
import os

class Board:
   """Game of Life Board"""
   grid = {}
   nextgrid = {}
   
   def __init__(self,p_x,p_y):
      for x in range(p_x):
         self.grid[x]={}
         for y in range(p_y):
            self.grid[x][y]=random.randint(0,1)

   def display(self):
      for y in range(len(self.grid[0])):
         for x in range(len(self.grid)):
            if (self.grid[x][y]==1):
               sys.stdout.write(" . ")
            else:
               sys.stdout.write("   ")
         sys.stdout.write("\n")
      sys.stdout.write("\n")

   def list_all_coords(self):
      for x in range(len(self.grid)):
         for y in range(len(self.grid[x])):
            print "x: {0} y: {1} value: {2}".format(x, y, self.grid[x][y])

   def get_live_neighbor_count(self,p_x,p_y):
      live_neighbors = 0
      for x in range(p_x-1,p_x+2):
         for y in range(p_y-1,p_y+2):
            if ( p_x == x and p_y == y ):  # skip myself
               live_neighbors += 0
            elif (x < 0 or y < 0 or x > len(self.grid)-1 or y > len(self.grid[0])-1 ):  # edge detection
               live_neighbors += 0
            else:
               if (self.grid[x][y]==1):
                  live_neighbors += 1
      return live_neighbors

   def process_rules(self,x,y):
      count = self.get_live_neighbor_count(x,y)
      alive = self.grid[x][y]
      if (alive == 1 and count >=2 and count <= 3) :
         self.nextgrid[x][y]=1
      elif ( alive == 0 and count == 3 ) :
         self.nextgrid[x][y]=1
   
   def next_turn(self):
      for x in range(len(self.grid)):
         self.nextgrid[x] = {}
         for y in range(len(self.grid[0])):
            self.nextgrid[x][y]=0
      
      for y in range(len(self.grid[0])):
         for x in range(len(self.grid)):
            self.process_rules(x,y)
      
      self.grid=self.nextgrid         
      self.nextgrid={}

iterations=0
os.system("clear")      
b = Board(40,40)
while (True):
   iterations += 1
   b.display()
   print "{0} iterations.".format(iterations)
   time.sleep(1)
   b.next_turn()
   os.system("clear")
