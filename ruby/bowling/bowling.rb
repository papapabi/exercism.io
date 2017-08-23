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
    if pins_knocked_down == 10
      f.add_to_frame(pins_knocked_down)
      f.wait_time(CASES[:strike])
      frames << Frame.new(f.number + 1)
    else
      if f.first_throw # exists
        f.add_to_frame(pins_knocked_down)
        if f.first_throw + f.second_throw == 10
          f.wait_time(CASES[:spare])
        else
          f.wait_time(CASES[:open])
        end
        frames << Frame.new(f.number + 1)
      else
        f.add_to_frame(pins_knocked_down)
      end
    end
    consolidate_frames
  end

  private

  def consolidate_frames
  end

  class Frame
    CASES =  { open: 0, spare: 1, strike: 2 }
    attr_reader :number, :score
    attr_accessor :first_throw
    attr_accessor :second_throw
    attr_accessor :wait_time

    def initialize(number)
      @number = number
      @score = 0 
    end

    def add_to_frame(pins_knocked_down)
      unless first_throw
        first_throw = pins_knocked_down 
      else
        second_throw = pins_knocked_down
        raise BowlingError if first_throw + second_throw > 10
      end
    end
  end

  private_constant :Frame, :CASES
end 
