import { TranslationProps } from '../../i18n'

interface InputProps extends TranslationProps {
  id: string,
  value: string,
  setter: (key: string, val: string) => void,
  side: 'left' | 'right',
  disabled?: boolean
}

export default function Input({t, id, value, setter, side, disabled = false}: InputProps) {
  return <div className={'d-flex flex-column m-sm-3 py-2 h6 ' + (side === 'left' ? 'ms-0' : 'me-0')}>
    <label className='text-secondary mb-2' htmlFor={id}>{t(id)}</label>
    {
      disabled
      ?
      <span className='w-100 border-0 border-bottom py-3'>{value ? value : <span className='text-white'>none</span>}</span>
      :
      <input className='py-3 px-4 border-0 border-bottom no-hover' value={value} onChange={e => setter(id, e.target.value)} />
    }
  </div>
}