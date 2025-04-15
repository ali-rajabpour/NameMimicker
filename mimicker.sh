#!/bin/bash

# Mimicker - Bash script for running the character mimicking tool
# Created for CEH certified research purposes
# Author: Ali Rajabpour Sanati
# Website: Rajabpour.com

# Colors for better UI
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PYTHON_SCRIPT="$SCRIPT_DIR/mimicker.py"

# Check if conda is installed
check_conda() {
    if ! command -v conda &> /dev/null; then
        echo -e "${RED}Error: Conda is not installed or not in PATH.${NC}"
        exit 1
    fi
}

# Check if the mimicker environment exists
check_env() {
    if ! conda env list | grep -q "mimicker"; then
        echo -e "${YELLOW}Mimicker environment not found. Creating it now...${NC}"
        conda create -y -n mimicker python=3.10
        echo -e "${GREEN}Environment created successfully.${NC}"
    fi
}

# Activate the mimicker environment and run a command
run_in_env() {
    # Use eval to properly handle the command
    eval "$(conda shell.bash hook)"
    conda activate mimicker
    eval "$@"
    conda deactivate
}

# Make sure the Python script is executable
make_executable() {
    if [ -f "$PYTHON_SCRIPT" ]; then
        chmod +x "$PYTHON_SCRIPT"
    else
        echo -e "${RED}Error: Python script not found at $PYTHON_SCRIPT${NC}"
        exit 1
    fi
}

# Run the mimicker tool with a string
run_mimicker() {
    local input_string="$1"
    local advanced="$2"
    local export_file="$3"
    local show_scores="$4"
    
    if [ -z "$input_string" ]; then
        echo -e "${YELLOW}Please enter a string to mimic:${NC} "
        read input_string
    fi
    
    if [ -n "$input_string" ]; then
        echo -e "${BLUE}Running mimicker with input: ${CYAN}$input_string${NC}"
        
        # Build command with optional parameters
        cmd="python $PYTHON_SCRIPT --string \"$input_string\""
        
        if [ "$advanced" = "true" ]; then
            cmd="$cmd --advanced"
        fi
        
        if [ "$show_scores" = "true" ]; then
            cmd="$cmd --scores"
        fi
        
        if [ -n "$export_file" ]; then
            cmd="$cmd --export \"$export_file\""
        fi
        
        run_in_env "$cmd"
    else
        echo -e "${RED}No input provided. Exiting.${NC}"
    fi
}

# Show help information
show_help() {
    echo -e "${CYAN}======================================================${NC}"
    echo -e "${CYAN}                  MIMICKER HELP                       ${NC}"
    echo -e "${CYAN}======================================================${NC}"
    echo -e "${GREEN}Mimicker${NC} is a tool for generating lookalike strings using"
    echo -e "different character sets for security research purposes."
    echo -e ""
    echo -e "${YELLOW}Usage:${NC}"
    echo -e "  ./mimicker.sh [command] [options]"
    echo -e ""
    echo -e "${YELLOW}Commands:${NC}"
    echo -e "  ${GREEN}run${NC} [string]    - Run the mimicker with optional input string"
    echo -e "  ${GREEN}advanced${NC} [string] - Run with advanced obfuscation techniques"
    echo -e "  ${GREEN}export${NC} [string] [file] - Export results to a JSON file"
    echo -e "  ${GREEN}help${NC}            - Show this help information"
    echo -e "  ${GREEN}setup${NC}           - Setup the conda environment"
    echo -e "  ${GREEN}menu${NC}            - Show the interactive menu (default)"
    echo -e ""
    echo -e "${YELLOW}Examples:${NC}"
    echo -e "  ./mimicker.sh run \"Apple\""
    echo -e "  ./mimicker.sh advanced \"Apple\""
    echo -e "  ./mimicker.sh export \"Apple\" results.json"
    echo -e "${CYAN}======================================================${NC}"
}

# Show the commands that were used to set up the project
show_commands() {
    echo -e "${CYAN}======================================================${NC}"
    echo -e "${CYAN}             SETUP COMMANDS USED                      ${NC}"
    echo -e "${CYAN}======================================================${NC}"
    echo -e "${YELLOW}# Create conda environment${NC}"
    echo -e "conda create -y -n mimicker python=3.10"
    echo -e ""
    echo -e "${YELLOW}# Activate environment${NC}"
    echo -e "conda activate mimicker"
    echo -e ""
    echo -e "${YELLOW}# Create project structure${NC}"
    echo -e "mkdir -p mimicker"
    echo -e ""
    echo -e "${YELLOW}# Create Python script${NC}"
    echo -e "# Created mimicker.py with character set mimicking functionality"
    echo -e ""
    echo -e "${YELLOW}# Create bash script${NC}"
    echo -e "# Created mimicker.sh with menu-driven interface"
    echo -e ""
    echo -e "${YELLOW}# Make scripts executable${NC}"
    echo -e "chmod +x mimicker.py mimicker.sh"
    echo -e "${CYAN}======================================================${NC}"
}

# Display the menu
show_menu() {
    clear
    echo -e "${CYAN}======================================================${NC}"
    echo -e "${GREEN}         ███╗   ███╗██╗███╗   ███╗██╗ ██████╗██╗  ██╗███████╗██████╗ ${NC}"
    echo -e "${GREEN}         ████╗ ████║██║████╗ ████║██║██╔════╝██║ ██╔╝██╔════╝██╔══██╗${NC}"
    echo -e "${GREEN}         ██╔████╔██║██║██╔████╔██║██║██║     █████╔╝ █████╗  ██████╔╝${NC}"
    echo -e "${GREEN}         ██║╚██╔╝██║██║██║╚██╔╝██║██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗${NC}"
    echo -e "${GREEN}         ██║ ╚═╝ ██║██║██║ ╚═╝ ██║██║╚██████╗██║  ██╗███████╗██║  ██║${NC}"
    echo -e "${GREEN}         ╚═╝     ╚═╝╚═╝╚═╝     ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝${NC}"
    echo -e "${CYAN}======================================================${NC}"
    echo -e "${CYAN}                MIMICKER MENU                         ${NC}"
    echo -e "${CYAN}======================================================${NC}"
    echo -e "${PURPLE}Author: Ali Rajabpour Sanati${NC}"
    echo -e "${PURPLE}Website: Rajabpour.com${NC}"
    echo -e "${CYAN}======================================================${NC}"
    echo -e "${YELLOW}1.${NC} Run Mimicker (Basic)"
    echo -e "${YELLOW}2.${NC} Run Mimicker (Advanced)"
    echo -e "${YELLOW}3.${NC} Export Results to File"
    echo -e "${YELLOW}4.${NC} Show Help"
    echo -e "${YELLOW}5.${NC} Setup Environment"
    echo -e "${YELLOW}6.${NC} Show Setup Commands"
    echo -e "${YELLOW}7.${NC} Exit"
    echo -e "${CYAN}======================================================${NC}"
    echo -e "Enter your choice [1-7]: "
    read choice
    
    case $choice in
        1)
            echo -e "${YELLOW}Enter a string to mimic (e.g., 'Apple'):${NC} "
            read input_string
            run_mimicker "$input_string" "false" "" "false"
            echo -e "\n${GREEN}Press Enter to return to the menu...${NC}"
            read
            show_menu
            ;;
        2)
            echo -e "${YELLOW}Enter a string to mimic (e.g., 'Apple'):${NC} "
            read input_string
            run_mimicker "$input_string" "true" "" "true"
            echo -e "\n${GREEN}Press Enter to return to the menu...${NC}"
            read
            show_menu
            ;;
        3)
            echo -e "${YELLOW}Enter a string to mimic (e.g., 'Apple'):${NC} "
            read input_string
            echo -e "${YELLOW}Enter export filename (e.g., 'results.json'):${NC} "
            read export_file
            run_mimicker "$input_string" "true" "$export_file" "true"
            echo -e "\n${GREEN}Press Enter to return to the menu...${NC}"
            read
            show_menu
            ;;
        4)
            show_help
            echo -e "\n${GREEN}Press Enter to return to the menu...${NC}"
            read
            show_menu
            ;;
        5)
            check_conda
            check_env
            make_executable
            echo -e "${GREEN}Setup completed successfully.${NC}"
            echo -e "\n${GREEN}Press Enter to return to the menu...${NC}"
            read
            show_menu
            ;;
        6)
            show_commands
            echo -e "\n${GREEN}Press Enter to return to the menu...${NC}"
            read
            show_menu
            ;;
        7)
            echo -e "${GREEN}Exiting Mimicker. Goodbye!${NC}"
            exit 0
            ;;
        *)
            echo -e "${RED}Invalid choice. Please try again.${NC}"
            sleep 2
            show_menu
            ;;
    esac
}

# Main function to handle command line arguments
main() {
    # Make sure the script is executable
    make_executable
    
    # Process command line arguments
    if [ $# -eq 0 ]; then
        # No arguments, show the menu
        show_menu
    else
        case "$1" in
            run)
                run_mimicker "${2:-}" "false" "" "false"
                ;;
            advanced)
                run_mimicker "${2:-}" "true" "" "true"
                ;;
            export)
                if [ -z "$3" ]; then
                    echo -e "${RED}Error: Export filename required.${NC}"
                    show_help
                    exit 1
                fi
                run_mimicker "${2:-}" "true" "$3" "true"
                ;;
            help)
                show_help
                ;;
            setup)
                check_conda
                check_env
                echo -e "${GREEN}Setup completed successfully.${NC}"
                ;;
            menu)
                show_menu
                ;;
            *)
                echo -e "${RED}Unknown command: $1${NC}"
                show_help
                exit 1
                ;;
        esac
    fi
}

# Run the main function
main "$@" 