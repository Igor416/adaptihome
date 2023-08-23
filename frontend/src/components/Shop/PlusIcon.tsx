interface PlusIconProps {
  size: number,
  active: boolean
}

export default function PlusIcon({size, active}: PlusIconProps) {
  return <div style={{width: size + 'vh', aspectRatio: 1}} className='position-relative'>
    <div style={{
      height: '2px',
      transform: `rotate(${active ? '180deg' : '0deg'})`
    }} className='w-100 transition bg-black position-absolute'></div>
    <div style={{
      height: '2px',
      transform: `rotate(${active ? '180deg' : '90deg'})`
    }} className='w-100 transition bg-black position-absolute'></div>
  </div>
}