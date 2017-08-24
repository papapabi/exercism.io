require_relative 'bowling_error'
require_relative 'frame'

# A class that models how a bowling game is scored.
class Game
  attr_reader :frames, :score
  def initialize
    @frames = [] << Frame.new(1)
    @score = 0
  end

  def roll(pins_knocked_down)
    raise BowlingError unless (0..10).include? pins_knocked_down
    f = frames.last
    f.add_to_frame(pins_knocked_down)
    if f.number == 10
      # Don't advance, stay put.
      # Game over when three balls are thrown at the best case when
      # a player throws a strike or a spare. 
    end
    if f.strike? || f.first_throw
      frames << Frame.new(f.number + 1)
    end
  end
end

def score
  frames.reduce(0) do |acc, f|
  end
end
