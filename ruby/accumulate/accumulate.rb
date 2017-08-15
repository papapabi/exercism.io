module Enumerable
  def accumulate()
    if block_given?
      [].tap { |accumulator| each { |e| accumulator << yield(e) } }
    else
      to_enum(:accumulate)
    end
  end
end

module BookKeeping
  VERSION = 1
end

