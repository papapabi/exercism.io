require_relative 'frame'
require_relative 'bowling_error'

class TenthFrame < Frame
  attr_reader :bonus
  attr_reader :number

  def initialize(number)
    super(number)
    @bonus = 0
  end

  def add(pins_knocked_down)
    if rolls == 0
      @first = pins_knocked_down
    elsif rolls == 1
      @second = pins_knocked_down
    elsif rolls == 2
      @bonus = pins_knocked_down
    else 
      raise BowlingError
    end
    @roll_tracker += 1
  end

  def bonus?
    if rolls == 1
      strike?
    elsif rolls == 2
      spare? || strike?
    else 
      # no bonus, end game
    end
  end

  def total
    first + second + bonus
  end
end
