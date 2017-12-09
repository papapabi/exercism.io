class Bst
  include Enumerable
  attr_reader :root

  def initialize(n)
    @root = Node.new(n)
  end

  def insert(n)
    root.insert(n)
  end

  def data
    root.data
  end

  def left
    root.left
  end

  def right
    root.right
  end

  class Node
    attr_accessor :left, :right
    attr_reader :data

    def initialize(left = nil, right = nil, data)
      @left = left 
      @right = right 
      @data = data 
    end

    def insert(new_data)
      new_node = Node.new(new_data)
      if new_data <= data
        left.nil? ? @left = new_node : @left.insert(new_data)
      elsif new_data > data
        right.nil? ? @right = new_node : @right.insert(new_data)
      end
    end
  end

  private_constant :Node
end
