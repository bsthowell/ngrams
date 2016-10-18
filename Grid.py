#!/usr/bin/env python
#floating point issues (0.1 is not exactly representable)
import math

class Grid:
   'class for grid data structure'
   #initial value in all cells
   INIT_VAL = 0

   #x and y ranges need to be divisible by their respective step sizes
   def __init__(self, x_start, x_end, x_step, y_start, y_end, y_step):
      self.x_start = x_start
      self.x_end = x_end
      self.x_step = x_step
      self.x_round_prec = int(math.ceil(math.log(1/self.x_step, 10)))
      self.y_start = y_start
      self.y_end = y_end
      self.y_step = y_step
      self.y_round_prec = int(math.ceil(math.log(1/self.y_step, 10)))
      num_x_buckets = int((float(x_end) - float(x_start)) / float(x_step)) + 1
      num_y_buckets = int((float(y_end) - float(y_start)) / float(y_step)) + 1
      self.data = [[self.INIT_VAL for y in range(0, num_y_buckets)] for x in range(0, num_x_buckets)]
      #self.data = [[(x,y) for y in range(0, num_y_buckets)] for x in range(0, num_x_buckets)]
   

   def index_from_coord(self, x,y):
      x_index = (x - self.x_start) / self.x_step
      y_index = (y - self.y_start) / self.y_step
      return int(round(x_index,0)), int(round(y_index,0))

   def coord_from_index(self, x_index, y_index):
      x = self.x_start + (x_index * self.x_step)
      y = self.y_start + (y_index * self.y_step)
      x = round(x, self.x_round_prec)
      y = round(y, self.y_round_prec)
      return x, y

   #coordinates must be integer multiples of step plus start
   #x and y must fall between respective starts and ends
   def insert(self, x, y, val):
      x_index, y_index = self.index_from_coord(x,y)
      self.data[x_index][y_index] = val

   #test
   def get(self, x, y):
      x_index, y_index = self.index_from_coord(x,y)
      return self.data[x_index][y_index]

   #equal sized grids. divides self by grid_b
   def divideGrid(self, grid_b_instance):
      grid_a = self.data
      grid_b = grid_b_instance.data

      for x in range(0, len(grid_a)):
         for y in range(0, len(grid_a)):
            grid_a_entry = grid_a[x][y]
            grid_b_entry = grid_b[x][y]
            if grid_b_entry == 0:
               #grid_a_entry should also be zero
               grid_a[x][y] = 0
            else:
               grid_a[x][y] = grid_a_entry / grid_b_entry


   def displayGrid(self):
      grid_data = self.data

      for x in range(0, len(grid_data)):
         for y in range(0, len(grid_data[0])):
            year, occ = self.coord_from_index(x,y)
            av_grad = grid_data[x][y]
            print(year, occ, av_grad)
