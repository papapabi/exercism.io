require 'prime'

class Raindrops
  def self.convert(num)
    out = { 3 => "Pling", 5 => "Plang", 7 => "Plong" }
    .select { |k, v| num % k == 0 }
    out.empty? ? num.to_s : out.values.join
  end
end
