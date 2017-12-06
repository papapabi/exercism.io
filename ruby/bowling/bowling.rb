require_relative 'bowling_error'
require_relative 'frame'
require_relative 'tenth_frame'

# A class that models how a bowling game is scored.
class Game
  attr_reader :frames
  attr_reader :pins_at_play

  def initialize
    @frames = [] << Frame.new(1)
    @pins_at_play = 10
  end

  def roll(pins_knocked_down)
    # Guard statements
    raise BowlingError.new('sobra rolls') if current_frame.number > 10
    raise BowlingError.new('roll must be in [0, 10]') unless (0..10).include? pins_knocked_down
    raise BowlingError.new('cannot knock down more pins than ones at play') if @pins_at_play - pins_knocked_down < 0

    @pins_at_play -= pins_knocked_down
    current_frame.add(pins_knocked_down)

    if current_frame.tenth? 
      if current_frame.strike? && @flag.nil?
        @pins_at_play = 10
        @flag = true
      elsif current_frame.second_strike? || current_frame.spare?
        @pins_at_play = 10
      else
        # ewan pa
      end
    end

    advance if current_frame.finished?
  end

  def score
    raise BowlingError.new("Cannot score incomplete games") unless frames.size >= 10 
    listeners = []
    frames.reduce(0) do |acc, f|
      listeners.each do |l|
        if l.wait - f.rolls >= 0
          acc += f.total
        else
          acc += f.tally(l.wait)
        end
        l.wait = l.wait - f.rolls
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
    if current_frame.number + 1 == 10
      @frames << TenthFrame.new(current_frame.number + 1)
    else
      @frames << Frame.new(current_frame.number + 1)
    end
    @pins_at_play = 10
  end
end

module BookKeeping
  VERSION = 3
end
