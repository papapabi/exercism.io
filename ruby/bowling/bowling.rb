require_relative 'bowling_error'
require_relative 'frame'

# A class that models how a bowling game is scored.
class Game
  attr_reader :frames
  def initialize
    @frames = [] << Frame.new(1)
  end

  def roll(pins_knocked_down)
    raise BowlingError unless (0..10).include? pins_knocked_down
    if current_frame.number == 10
      current_frame.add(pins_knocked_down)
    else
      current_frame.add(pins_knocked_down)
      advance if current_frame.finished?
    end
  end

  def score
    frames.reduce(0) do |acc, f|
      acc += f.total
    end
  end

  def current_frame
    @frames.last
  end

  def advance
    @frames << Frame.new(current_frame.number)
  end
end
