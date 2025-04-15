# tf.keras.layers.Layer 상속
# 텐서플로우에서 사용자 정의 레이어를 만들고 싶을 때 사용하는 기반 클래스    
class PositionalEncoding(tf.keras.layers.Layer):
  
  # position : 문장의 최대 길이
  # d_model : 딘어 벡터의 차원 수.
  def __init__(self, position, d_model): # 생성자.
    # 부모 클래스의 생성자 실행
    super(PositionalEncoding, self).__init__()

    # 이 클래스의 최종 목적. pos_encoding 값
    self.pos_encoding = self.positional_encoding(position, d_model)

  # 포지셔널 인코딩의 핵심 수식
  # 그 사인, 코사인 연산 하기 전, pos/10000**(2i/d_model)) 연산
  # 사인/코사인 입력 값이 곧 위치 정보가 되게 하기 위해 , return 값을 position과 angle값을 곱함. <<= ? 뭔소리야
  def get_angles(self, position, i, d_model):
    angles = 1 / tf.pow(10000, (2 * (i // 2)) / tf.cast(d_model, tf.float32))
    return position * angles

  # 포지셔널 인코딩 연산 = 입력 벡터 + 포지셔널 인코딩 벡터 (행렬 덧셈)

  def positional_encoding(self, position, d_model):
    angle_rads = self.get_angles(
        position=tf.range(position, dtype=tf.float32)[:, tf.newaxis], # position = 문장 내 위치 인덱스를 생성
        i=tf.range(d_model, dtype=tf.float32)[tf.newaxis, :], # 임베딩 차원 인덱스를 만듬
        
        d_model=d_model)

    # 배열의 짝수 인덱스(2i)에는 사인 함수 적용
    sines = tf.math.sin(angle_rads[:, 0::2])

    # 배열의 홀수 인덱스(2i+1)에는 코사인 함수 적용
    cosines = tf.math.cos(angle_rads[:, 1::2])

    # 사인과 코사인 결과를 합쳐서 최종 포지셔널 인코딩 배열을 구성함.
    angle_rads = np.zeros(angle_rads.shape)
    angle_rads[:, 0::2] = sines
    angle_rads[:, 1::2] = cosines

    # [1, position, d_model] 형태로 reshape → 배치 차원을 앞에 추가 <<-- 얜 잘 모르겠네
    pos_encoding = tf.constant(angle_rads)
    pos_encoding = pos_encoding[tf.newaxis, ...]

    print(pos_encoding.shape)
    # 반환
    return tf.cast(pos_encoding, tf.float32)

  # 만들어진 최종 포지셔널 인코딩 배열과 입력 인베딩 값을 더해주는 형태
  def call(self, inputs):
    return inputs + self.pos_encoding[:, :tf.shape(inputs)[1], :]
  



# 문장의 길이 50, 임베딩 벡터의 차원 128
sample_pos_encoding = PositionalEncoding(50, 128)

plt.pcolormesh(sample_pos_encoding.pos_encoding.numpy()[0], cmap='RdBu')
plt.xlabel('Depth')
plt.xlim((0, 128))
plt.ylabel('Position')
plt.colorbar()
plt.show()