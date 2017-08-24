require_relative 'bowling_error'

class Frame
  attr_reader :number, :score
  attr_reader :first_throw, :second_throw, :third_throw

  def initialize(number)
    @number = number
    @score = 0 
  end

  def add_to_frame(pins_knocked_down)
    if number == 10 # Special case for the tenth bowling frame
      if first_throw.nil?
        first_throw = pins_knocked_down
      elsif second_throw.nil?
        second_throw = pins_knocked_down
      else 
        third_throw = pins_knocked_down
      end
    else 
      unless first_throw
        first_throw = pins_knocked_down 
      else
        second_throw = pins_knocked_down
        raise BowlingError if first_throw + second_throw > 10
      end
    end
  end

  def strike?
    first_throw == 10
  end

  def spare?
    first_throw + second_throw == 10
  end

  def open?
    first_throw + second_throw < 10
  end

  def to_s
    [number, first_throw, second_throw, third_throw, score]
  end

  private_constant :Frame
end 
