class ETL
  def self.transform(old)
    new = {}
    old.each do |key, values|
      values.each do |value|
        new[value.downcase] = key
      end
    end
    new
  end
end

module BookKeeping
  VERSION = 1
end
