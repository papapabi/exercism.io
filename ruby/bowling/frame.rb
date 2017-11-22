require_relative 'bowling_error'

class Frame
  attr_reader :first, :second, :bonus
  attr_reader :roll_tracker
  attr_reader :number

  def initialize(number)
    @number = number
    @first = @second = @bonus = @roll_tracker = 0
  end

  def add(pins_knocked_down)
    if roll_tracker == 0
      @first = pins_knocked_down
    elsif roll_tracker == 1
      @second = pins_knocked_down
    elsif roll_tracker == 2
      @bonus = pins_knocked_down
    end
    @roll_tracker += 1
  end


  def strike?
    first == 10
  end

  def spare?
    first + second == 10
  end

  def open?
    first + second < 10
  end

  def total
    first + second + bonus
  end

  def to_s
    [number, first, second, bonus, score]
  end

  def finished?
    if number == 10
      !spare? || roll_tracker >= 2
    else 
      strike? || roll_tracker >= 1
    end
  end
end 
