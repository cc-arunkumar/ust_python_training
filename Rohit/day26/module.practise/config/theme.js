export let theme  = "light"

export function toggleTheme(value){
    theme = value
    theme= theme==="light"?"dark":"light"
    return theme
}
