class Gigasecond
  GIGASECOND = 10**9 
  def self.from(birth_date)
    (birth_date.to_time + GIGASECOND).to_time
  end
end
