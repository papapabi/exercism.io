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
    listeners = []
    frames.reduce(0) do |acc, f|
      listeners.each do |l|
        l.wait =  l.wait - f.rolls
        if l.wait >= 0
          acc += f.total
        else
          acc += f.first
        end
      end

      listeners.delete_if { |l| l.wait <= 0 }

      if f.strike? || f.spare?
        listeners << f
      end
      acc += f.total
    end
  end

  def current_frame
    @frames.last
  end

  def advance
    @frames << Frame.new(current_frame.number + 1)
  end
end

module BookKeeping
  VERSION = 3
end
