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
    raise BowlingError unless (0..10).include? pins_knocked_down
    raise BowlingError if @pins_at_play - pins_knocked_down < 0
    @pins_at_play -= pins_knocked_down

    if current_frame.tenth?
      current_frame.add(pins_knocked_down)
      if current_frame.bonus?
        @pins_at_play = 10
      else
        return # the game has ended
      end
    else
      current_frame.add(pins_knocked_down)
      advance if current_frame.finished?
    end
  end

  def score
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

  # Advance to the next frame
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
