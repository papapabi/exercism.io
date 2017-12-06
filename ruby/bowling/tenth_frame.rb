require_relative 'frame'
require_relative 'bowling_error'

class TenthFrame < Frame
  attr_reader :number
  attr_reader :bonus

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
    strike? || spare?
  end

  def finished?
    if bonus?
      rolls == 3
    else
      rolls == 2
    end
  end

  def flagged?
    @flagged ||= true
  end

  def spare?
    first + second == 10 && first != 10
  end

  def second_strike?
    second == 10
  end

  def total
    first + second + bonus
  end
end
