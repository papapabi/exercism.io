class Sieve
  def initialize(max_bound)
    @lookup_table = {}
    (2..max_bound).each { |i| @lookup_table[i] = false }
  end

  def primes
    @lookup_table.keys.each do |key|
      next if @lookup_table[key] 
      @lookup_table.each do |k, v| 
        next if k <= key 
        @lookup_table[k] = true if k % key == 0 
      end
    end
    @primes = @primes || @lookup_table.select { |k, v| v == false }.keys.to_a
  end
end
