class PhoneNumber
  def self.clean(n)
    digits = get_digits(n) 
    if valid?(digits)
      if digits.length == 11
        remove_area_code(digits)
      else
        digits
      end
    else
      nil
    end
  end

  private
  class << self
    def get_digits(n)
      n.scan(/\d/).join 
    end

    def valid?(n)
      /\b(\+)?(1)?[2-9]\d{2}[2-9]\d{6}\b/ =~ n
    end

    def remove_area_code(n)
      n[0] = ''
      n
    end
  end
end

module BookKeeping
  VERSION = 2
end
