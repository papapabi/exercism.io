class Year
  # Checks if the year given as an integer argument is a leap year.
  def self.leap?(year)
    return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)
  end
end

module BookKeeping
  VERSION = 3
end

