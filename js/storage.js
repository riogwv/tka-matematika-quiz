export function storage(key,fallback){try{return JSON.parse(localStorage.getItem('tka-math-v1-'+key))??fallback;}catch{return fallback;}}
export function persist(key,value){try{localStorage.setItem('tka-math-v1-'+key,JSON.stringify(value));return true;}catch{return false;}}
